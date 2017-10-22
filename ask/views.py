# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic import TemplateView

def parseParams(query):
    return ''.join('<h1>{} = {}</h1>'.format(i, query[i]) for i in query)


#Данный метод может выполняться без подтверждения CSRF токена с помощью этого декоратора
@csrf_exempt
def requestsPrint(request):
	print('it was me')
	printingString = parseParams(request.GET) + parseParams(request.POST)
	return HttpResponse(printingString)

class indexPage(TemplateView):
	print('it was me')
	template_name = "about.html"
