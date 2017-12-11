# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth import authenticate, login

from ask.models import *
from .forms import UserSignUpForm


def signin(request):
    return render(request, 'signin.html')


def signup(request):
    errors = []
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if request.POST['password'] != request.POST['password_confirmation']:
            errors.append('Passwords don\'t match')
        if form.is_valid():
            user = User.objects.create(username=request.POST['username'],
                                       email=request.POST['email'],
                                       first_name=request.POST['first_name'],
                                       last_name=request.POST['last_name'])
            user.set_password(request.POST['password_confirmation'])
            user.save()
            login(request, user)
            print(user.is_authenticated)
            return render(request, 'feed.html', {'messages': ['Thanks for registration']})
        else:
            for i in form.errors:
                errors.append(form._errors[i][0])

    else:
        form = UserSignUpForm

    return render(request, 'signup.html', {'form': form, 'messages': errors})


def question_detailed(request, question_id):
    return render(request, 'question_details.html', {'question': Question.objects.by_id(question_id).first()})


def questions_by_tag(request, **kwargs):
    return renderFeedWithPagination(request,
                                    header="По тегу: {}".format(kwargs.get('tag_str')),
                                    questions_list=Tag.objects.by_tag(kwargs.get('tag_str')))


def hottest(request):
    return renderFeedWithPagination(request,
                                    Question.objects.hottest(),
                                    header='Лучшее',
                                    link='/',
                                    link_text='Новое')


def new(request):
    return render(request, 'new_question.html')


def newest(request):
    return renderFeedWithPagination(request, Question.objects.newest(), header='Новое')


def renderFeedWithPagination(request, questions_list, header, link='/hot', link_text="Лучшее"):
    paginator = Paginator(questions_list, 4)

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # Если не запрошена никакая страница через GET параметры, то вернуть первую
        questions = paginator.page(1)
    except EmptyPage:
        # Если запрашиваемая страница больше, чем страниц всего.
        questions = paginator.page(paginator.num_pages)

    return render(request, 'feed.html',
                  {'header': header,
                   'questions_list': questions,
                   'link': link,
                   'link_text': link_text})
