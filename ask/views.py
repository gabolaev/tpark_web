# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from ask.models import *


def guest(request):
    return render(request, 'guest.html')


def signin(request):
    return render(request, 'signin.html')


def signup(request):
    return render(request, 'signup.html')


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


    # import random
    # import lorem
    #
    # for i in range(126, 525):
    #     try:
    #         q = Question.objects.by_id(i).first()
    #         for j in range(random.randint(1,10)):
    #             t = Tag.objects.get_or_create(title=max(lorem.sentence().split()))[0]
    #             q.tags.add(t)
    #             q.save()
    #     except Exception as e:
    #         print(e)

    # q = Question(author=u, title=lorem.sentence(), text=lorem.text())
    # print(pk)
    # q.tags.get_or_create(title='test')
    #
    # questions_list[str(i)] = {
    #     'id': i,
    #     'uid': random.randrange(1000),
    #     'avatar': 'avatars/user{}.png'.format(random.randrange(1, 8)),
    #     'username': names.get_first_name(),
    #     'title': lorem.sentence(),
    #     'text': lorem.text(),
    #     'date': '11.09.2001',
    #     'tags': },
    #     'likes': random.randrange(20000),
    #     'dislikes': random.randrange(20000),
    # }
