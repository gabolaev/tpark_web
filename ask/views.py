# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from ask.models import *
from .forms import *


def fillErrors(formErrors, errors):
    for i in formErrors:
        formattedFieldName = i.replace('_', ' ')
        errors.append(f' { formattedFieldName } field error: {formErrors[i][0]}')


@login_required(login_url='/signin/')
def profile(request, username):
    user = User.objects.by_username(username)
    if user is not None:
        return render(request, 'profile.html', {'profile': user})
    else:
        raise Http404


@login_required(login_url='/signin/')
def settings(request):
    errors = []
    form = UserSettingsForm
    if request.method == 'POST':
        form = form(request.POST)
        if form.is_valid():
            for changedField in form.changed_data:
                setattr(request.user, changedField, request.POST[changedField])
            request.user.save()
            return redirect('/profile/edit/')
        else:
            fillErrors(form.errors, errors)
    else:
        for i in form.base_fields:
            form.base_fields[i].widget.attrs['placeholder'] = getattr(request.user, i)
    return render(request, 'settings.html', {'form': form, 'messages': errors})


def signin(request):
    errors = []
    form = UserSignInForm
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next') if request.GET.get('next') != '' else '/')
        else:
            errors.append('Invalid username or password')

    logout(request)
    return render(request, 'signin.html', {'form': form, 'messages': errors})


def signout(request):
    if not request.user.is_authenticated:
        raise Http404
    logout(request)
    return redirect(request.GET['from'])


def signup(request):
    errors = []
    form = UserSignUpForm
    if request.method == 'POST':
        form = form(request.POST)
        if request.POST['password'] != request.POST['password_confirmation']:
            errors.append('Passwords don\'t match')
        elif form.is_valid():
            user = User.objects.create(username=request.POST['username'],
                                       email=request.POST['email'],
                                       first_name=request.POST['first_name'],
                                       last_name=request.POST['last_name'])
            user.set_password(request.POST['password_confirmation'])
            user.save()
            login(request, user)
            return redirect('/')
        else:
            fillErrors(form.errors, errors)
    else:
        logout(request)

    return render(request, 'signup.html', {'form': form, 'messages': errors})


def question_detailed(request, question_id):
    question = Question.objects.by_id(int(question_id)).first()
    if question is not None:
        return render(request, 'question_details.html', {'question': question})
    else:
        raise Http404


class VotesView(View):
    model = None  # Data Model - Articles or Comments
    vote_type = None  # Vote type Like/Dislike

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        #        GenericForeignKey does not support get_or_create
        try:
            like_dislike = Like.objects.get(content_type=ContentType.objects.get_for_model(obj),
                                            object_id=obj.id,
                                            user=request.user)

            if like_dislike.vote is not self.vote_type:
                like_dislike.vote = self.vote_type
                obj.rate += 2*self.vote_type
                like_dislike.save(update_fields=['vote'])
                result = True
            else:
                obj.rate -= self.vote_type
                like_dislike.delete()
                result = False
        except Like.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            obj.rate += self.vote_type
            result = True

        obj.save()
        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": obj.votes.likes().count(),
                "dislike_count": obj.votes.dislikes().count(),
                "sum_rating": obj.votes.sum_rating()
            }),
            content_type="application/json"
        )


def questions_by_tag(request, **kwargs):
    return renderFeedWithPagination(request,
                                    header="By tag: {}".format(kwargs.get('tag_str')),
                                    questions_list=Tag.objects.by_tag(kwargs.get('tag_str')))


def hottest(request):
    return renderFeedWithPagination(request,
                                    Question.objects.hottest(),
                                    header='Hottest🔥',
                                    link='/',
                                    link_text='Newest')


@login_required(login_url='/signin/')
def new(request):
    errors = []
    form = NewQuestionForm
    if request.method == 'POST':
        form = form(request.POST)

        if form.is_valid():
            question = Question.objects.create(author=request.user,
                                               date=timezone.now(),
                                               is_active=True,
                                               title=request.POST['title'],
                                               text=request.POST['text'])
            question.save()
            for tagTitle in request.POST['tags'].split():
                tag = Tag.objects.get_or_create(title=tagTitle)[0]
                question.tags.add(tag)
                question.save()
            return question_detailed(request, question.id)
        else:
            fillErrors(form.errors, errors)

    return render(request, 'new_question.html', {'form': form, 'messages': errors})


@login_required(login_url='/signin/')
def write_answer(request, question_id):
    errors = []
    form = WriteAnswerForm
    if Question.objects.filter(id=question_id).exists():
        if request.method == 'POST':
            form = form(request.POST)
            if form.is_valid():
                answeredQuestion = Question.objects.by_id(question_id)[0]
                newAnswer = Answer.objects.create(author=request.user,
                                                  date=timezone.now(),
                                                  text=request.POST['text'],
                                                  question_id=answeredQuestion.id)
                newAnswer.save()
                return redirect(f'/questions/{ question_id }/#{ newAnswer.id }')
            else:
                fillErrors(form.errors, errors)

        return render(request, 'answer.html', {'form': form, 'messages': errors})
    else:
        raise Http404


def newest(request):
    return renderFeedWithPagination(request, Question.objects.newest(), header='Newest')


def renderFeedWithPagination(request, questions_list, header, link='/hot', link_text="Hottest🔥"):
    paginator = Paginator(questions_list, 30)

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'feed.html',
                  {'header': header,
                   'questions_list': questions,
                   'link': link,
                   'link_text': link_text})
