from django.conf.urls import url

from ask.views import *

urlpatterns = [
    url(r'^$', feed),
    url(r'^questions/(?P<question_id>[0-9]+)/$', question_detailed, name='questions_detail'),
    url(r'^questions/tag/(?P<tag>\w+)/$', questions_by_tag, name='questions_detail'),
    url(r'^parse_request/.*', requestsPrint),
]
