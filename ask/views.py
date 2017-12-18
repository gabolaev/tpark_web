# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.shortcuts import render, redirect

from ask.models import *
from .forms import *


def fillErrors(formErrors, errors):
    for i in formErrors:
        formattedFieldName = i.replace('_', ' ')
        errors.append(f' { formattedFieldName } field error: {formErrors[i][0]}')


@login_required(login_url='/signin/')
def settings(request):
    errors = []
    if request.method == 'POST':
        form = UserSettingsForm(request.POST)
        if form.is_valid():
            if 'username' in form.changed_data:
                request.user.username = request.POST['username']
            if 'email' in form.changed_data:
                request.user.email = request.POST['email']

            request.user.save()
            return redirect('/')
        else:
            fillErrors(form.errors, errors)
    else:
        form = UserSettingsForm
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


@login_required(login_url='/signin/')
def signout(request):
    logout(request)
    return redirect('/')


def signup(request):
    errors = []
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
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
        form = UserSignUpForm

    return render(request, 'signup.html', {'form': form, 'messages': errors})


def question_detailed(request, question_id):
    question = Question.objects.by_id(int(question_id)).first()
    if question is not None:
        return render(request, 'question_details.html', {'question': question})
    else:
        raise Http404


def questions_by_tag(request, **kwargs):
    return renderFeedWithPagination(request,
                                    header="By tag: {}".format(kwargs.get('tag_str')),
                                    questions_list=Tag.objects.by_tag(kwargs.get('tag_str')))


def hottest(request):
    return renderFeedWithPagination(request,
                                    Question.objects.hottest(),
                                    header='Hottest',
                                    link='/',
                                    link_text='Newest')


@login_required(login_url='/signin/')
def new(request):
    errors = []
    if request.method == 'POST':
        form = NewQuestionForm(request.POST)

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
    else:
        form = NewQuestionForm

    return render(request, 'new_question.html', {'form': form, 'messages': errors})


@login_required(login_url='/signin/')
def write_answer(request, question_id):
    errors = []
    if Question.objects.filter(id=question_id).exists():
        if request.method == 'POST':
            form = WriteAnswerForm(request.POST)
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
        else:
            form = WriteAnswerForm

        return render(request, 'answer.html', {'form': form, 'messages': errors})
    else:
        raise Http404


def newest(request):
    return renderFeedWithPagination(request, Question.objects.newest(), header='Newest')


def renderFeedWithPagination(request, questions_list, header, link='/hot', link_text="Hottest"):
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
