from django.conf.urls import url

from ask.views import *

urlpatterns = [
	url(r'^$', indexPage.as_view()),
    url(r'^request/.*', requestsPrint),
]
