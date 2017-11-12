# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

QUESTIONS = {
    '1': {'id': 1,
          'uid': 2,
          'avatar': 'avatars/user1.png',
          'username': 'gabolaev',
          'title': 'How to exit from VIM',
          'text': 'I worked on the command line. I got into a strange text editor, in which the mouse does not work. I see the message "type: quit to quit VIM" But the command is written directly into a text file and is not executed. What to do, how to get out?',
          'date': '27.04.1998',
          'tags': {'terminal', 'vim', 'shit', 'hard'},
          'likes': 143,
          'dislikes': 9,
          },

    '2': {'id': 2,
          'uid': 3,
          'avatar': 'avatars/user2.png',
          'username': 'user500',
          'title': 'most efficient way to guarantee uniqueness when generating a large amount of random numbers [duplicate]',
          'text': """I need to generate an array of random numbers representing v4 ip address, and each random numbers in the array have to be unique.
What would be the most efficient approach (data structure and algorithm) to solve this problem?
I am thinking to generate an array of 255^4 element, from 0 to 255^4. and use a shuffle algorithm such as Fischer and Yattes algorithm to shuffle these number. So when I need to generate an array of n element, I simply pick the 1st n element from the above array.
Is it the most efficient approach?""",
          'date': '19.01.2000',
          'tags': {'java', 'numbers', 'shit'},
          'likes': 4367,
          'dislikes': 2828,
          },

    '3': {'id': 3,
          'uid': 3,
          'avatar': 'avatars/user4.png',
          'username': 'hamster',
          'title': 'What’s Happening With Channels?',
          'text': """Like we have done with other ongoing projects 1, 2, 3, we're going to try to provide regular announcements about Channels. For those who aren’t aware of what Channels is, we're working on:

a feature of Stack Overflow for organizations to have a private & secure space for their engineering teams to collaborate pretty much unrestricted and unstructured apart from public Q&A. Channels are for organizations both large and small and do not in any way affect public Q&A.
The response to the initial announcement was overwhelming, with over 2,500 signups from people telling us about their organization, and that they were interested in using Channels for their team. We have been pretty quiet since then, but I'm here to tell you a bit about where we are at, and what's next with Channels.

Since the announcement, the team has been hard at work figuring out everything that needs to be done in order to get Channels up and running. Most of this has been on the stuff that's hidden from view. It's the backend core architecture to get us an internal version to test on. We've gone from pushing the limits and trying to break things, like Nick Craver load testing SQL Server by putting 10k schemas and 1.5 million tables into one database to see what would happen, to actually breaking things...accidentally when Channels code was pushed into production. Over the past month, we were able to get a very rough internal dev version of Channels up for us to starting testing with, and after a ton of work we successfully got Channels in an isolated environment for the real dogfooding to begin.""",
          'date': '04.07.2016',
          'tags': {'UX', 'meta', 'interface', 'hard'},
          'likes': 1330,
          'dislikes': 1740,
          },
    '4': {'id': 4,
          'uid': 4,
          'avatar': 'avatars/user3.png',
          'username': 'friex',
          'title': 'How does this Man-In-The-Middle attack work?',
          'text': """The Django documentation on its CSRF protection states that:

In addition, for HTTPS requests, strict referer checking is done by CsrfViewMiddleware. This is necessary to address a Man-In-The-Middle attack that is possible under HTTPS when using a session independent nonce, due to the fact that HTTP 'Set-Cookie' headers are (unfortunately) accepted by clients that are talking to a site under HTTPS. (Referer checking is not done for HTTP requests because the presence of the Referer header is not reliable enough under HTTP.)
I have trouble visualizing how this attack works. Could somebody explain?

UPDATE:
The wording in the Django doc seems to imply that there is a specific type of man-in-the-middle attack (which leads to a successful CSRF I'd assume) that works with session independent nonce (but not with transaction specific nonce etc., I suppose) and involves the use of 'Set-Cookie' header.
So I wanted to know how that specific type of attack works.""",
          'date': '04.08.2016',
          'tags': {'breaking', 'stealing', 'the third', 'hard'},
          'likes': 0,
          'dislikes': 19,
          },

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


def feed(request):
    return render(request, 'feed.html', {'header': 'Новые вопросы', 'questions_list': QUESTIONS.values()})


def question_detailed(request, question_id):
    return render(request, 'question_details.html', {'question': QUESTIONS[question_id]})


def questions_by_tag(request, tag):
    return render(request, 'feed.html', {'header': 'По тегу: {}'.format(tag),
                                         'questions_list': [QUESTIONS[i] for i in QUESTIONS if
                                                            tag in QUESTIONS[i]['tags']]})
