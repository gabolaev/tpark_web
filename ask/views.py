# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

import lorem
import names
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

questions_list = {
    '1': {
        'id': 1,
        'uid': 2,
        'avatar': 'avatars/user1.png',
        'username': 'gabolaev',
        'title': 'How to exit from VIM',
        'text': 'I worked on the command line. I got into a strange text editor, in which the mouse does not work. I see the message "type: quit to quit VIM" But the command is written directly into a text file and is not executed. What to do, how to get out?',
        'date': '27.04.1998',
        'tags': {
            'shit',
            'vim',
            'hard',
            'terminal'
        },
        'likes': 143,
        'dislikes': 9,
        'answers': {
            '1': {
                'uid': 2,
                'avatar': 'avatars/user2.png',
                'username': 'user500',
                'likes': 198,
                'dislikes': 123,
                'text': '\nHit the Esc key to enter "Command mode". Then you can type : to enter "Command-line mode". A colon (:) will appear at the bottom of the screen and you can type in one of the following commands. To execute a command, press the Enter key.\n\n:q to quit (short for :quit)\n:q! to quit without saving (short for :quit!)\n:wq to write and quit\n:wq! to write and quit even if file has only read permission (if file does not have write permission: force write)\n:x to write and quit (similar to :wq, but only write if there are changes)\n:exit to write and exit (same as :x)\n:qa to quit all (short for :quitall)\nYou can also exit Vim directly from "Command mode" by typing ZZ to save and quit (same as :x) or ZQ to just quit (same as :q!). (Note that case is important here. ZZ and zz do not mean the same thing.)\n\nVim has extensive help - that you can access with the :help command - where you can find answers to all your questions and a tutorial for beginners.'
            },
            '2': {
                'uid': 3,
                'avatar': 'avatars/user4.png',
                'username': 'hamster',
                'likes': 19218,
                'dislikes': 12,
                'text': "\nBefore you enter a command, hit the Esc key. After you enter it, hit the Return to confirm.\n\nEsc finishes the current command and switches Vim to command-line mode. Now if you press :, the : will appear at the bottom of the screen. This confirms that you're actually typing a command and not editing the file.\n\nMost commands have abbreviations, with optional part enclosed in brackets: c[ommand].\n\nCommands marked with '*' are Vim-only (not implemented in Vi).\n\nSafe-quit (fails if there are unsaved changes):\n\n:q[uit] Quit the current window. Quit Vim if this is the last window. This fails when changes have been made in current buffer.\n:qa[ll]* Quit all windows and Vim, unless there are some buffers which have been changed.\nPrompt-quit (prompts if there are unsaved changes)\n\n:conf[irm] q[uit]* Quit, but give prompt when there are some buffers which have been changed.\n:conf[irm] xa[ll]* Write all changed buffers and exit Vim. Bring up a prompt when some buffers cannot be written.\nWrite (save) changes and quit:\n\n:wq Write the current file (even if it was not changed) and quit. Writing fails when the file is read-only or the buffer does not have a name. :wqa[ll]* for all windows.\n:wq! The same, but writes even read-only files. :wqa[ll]!* for all windows.\n:x[it], ZZ(with details). Write the file only if it was changed and quit, :xa[ll]* for all windows.\nDiscard changes and quit:\n\n:q[uit]! ZQ* Quit without writing, also when visible buffers have changes. Does not exit when there are changed hidden buffers.\n:qa[ll]!*, :quita[ll][!]* Quit Vim, all changes to the buffers (including hidden) are lost.\nPress Return to confirm the command.\n\nThis answer doesn't reference all Vim write and quit commands and arguments. Indeed, they are referenced in the Vim documentation.\n\nVim has extensive built-in help, type Esc:helpReturn to open it."
            },
            '3': {
                'uid': 4,
                'avatar': 'avatars/user3.png',
                'username': 'friex',
                'likes': 412,
                'dislikes': 18923,
                'text': "\nI got Vim by installing a Git client on Windows. :q wouldn't exit Vim for me. :exit did however..."
            }
        }
    },
    '2': {
        'id': 2,
        'uid': 3,
        'avatar': 'avatars/user2.png',
        'username': 'user500',
        'title': 'most efficient way to guarantee uniqueness when generating a large amount of random numbers [duplicate]',
        'text': 'I need to generate an array of random numbers representing v4 ip address, and each random numbers in the array have to be unique.\nWhat would be the most efficient approach (data structure and algorithm) to solve this problem?\nI am thinking to generate an array of 255^4 element, from 0 to 255^4. and use a shuffle algorithm such as Fischer and Yattes algorithm to shuffle these number. So when I need to generate an array of n element, I simply pick the 1st n element from the above array.\nIs it the most efficient approach?',
        'date': '21.02.2011',
        'tags': {
            'java',
            'shit',
            'numbers'
        },
        'likes': 127983,
        'dislikes': 12
    },
    '3': {
        'id': 3,
        'uid': 3,
        'avatar': 'avatars/user4.png',
        'username': 'hamster',
        'title': 'What’s Happening With Channels?',
        'text': "Like we have done with other ongoing projects 1, 2, 3, we're going to try to provide regular announcements about Channels. For those who aren’t aware of what Channels is, we're working on:\n\na feature of Stack Overflow for organizations to have a private & secure space for their engineering teams to collaborate pretty much unrestricted and unstructured apart from public Q&A. Channels are for organizations both large and small and do not in any way affect public Q&A.\nThe response to the initial announcement was overwhelming, with over 2,500 signups from people telling us about their organization, and that they were interested in using Channels for their team. We have been pretty quiet since then, but I'm here to tell you a bit about where we are at, and what's next with Channels.\n\nSince the announcement, the team has been hard at work figuring out everything that needs to be done in order to get Channels up and running. Most of this has been on the stuff that's hidden from view. It's the backend core architecture to get us an internal version to test on. We've gone from pushing the limits and trying to break things, like Nick Craver load testing SQL Server by putting 10k schemas and 1.5 million tables into one database to see what would happen, to actually breaking things...accidentally when Channels code was pushed into production. Over the past month, we were able to get a very rough internal dev version of Channels up for us to starting testing with, and after a ton of work we successfully got Channels in an isolated environment for the real dogfooding to begin.",
        'date': '04.07.2016',
        'tags': {
            'meta',
            'interface',
            'hard',
            'UX'
        },
        'likes': 133022,
        'dislikes': 1740
    },
}

# let's create some fake data)))
for i in range(4, 40):
    questions_list[str(i)] = {
        'id': i,
        'uid': random.randrange(1000),
        'avatar': 'avatars/user{}.png'.format(random.randrange(1, 8)),
        'username': names.get_first_name(),
        'title': lorem.sentence(),
        'text': lorem.text(),
        'date': '11.09.2001',
        'tags': {max(lorem.sentence().split()) for i in range(random.randrange(10))},
        'likes': random.randrange(20000),
        'dislikes': random.randrange(20000),
    }


def parseParams(query):
    return ''.join('<h1>{} = {}</h1>'.format(i, query[i]) for i in query)


def handle_uploaded_file(f):
    with open('uploads/name.jpg', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@csrf_exempt
def requestsPrint(request):
    print('it was me')
    printingString = parseParams(request.GET) + parseParams(request.POST) + parseParams(request.FILES)
    # if request.FILES.__len__():
    #     file = request.FILES['file']
    #     handle_uploaded_file(file)
    #     return HttpResponse(content=file, content_type="image/jpg")
    # else:
    return HttpResponse(printingString)


def guest(request):
    return render(request, 'guest.html')


def signin(request):
    return render(request, 'signin.html')


def signup(request):
    return render(request, 'signup.html')


def question_detailed(request, question_id):
    return render(request, 'question_details.html', {'question': questions_list[question_id]})


# TODO: make tags clickable
def questions_by_tag(request, tag):
    return renderFeedWithPagination(request,
                                    header="По тегу: {}".format(tag),
                                    questions_list=dict(enumerate([questions_list[i] for i in questions_list if
                                                                   tag in questions_list[i]['tags']])))


def hottest(request):
    return renderFeedWithPagination(request,
                                    dict(enumerate(
                                        sorted(questions_list.values(), key=lambda x: x['likes'] / x['dislikes']))),
                                    header='Лучшее',
                                    link='/',
                                    link_text='Главная')


def new(request):
    return render(request, 'new_question.html')


def newest(request):
    return renderFeedWithPagination(request, questions_list, header='Новые вопросы')


def renderFeedWithPagination(request, questions_list, header, link='/hot', link_text="Лучшее"):
    contact_list = list(questions_list.values())[::-1]
    paginator = Paginator(contact_list, 4)

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
