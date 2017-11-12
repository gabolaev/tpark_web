from django.conf.urls import url

from ask.views import *

app_name = 'ask'
urlpatterns = [
    url(r'^$', newest, name='newest'),
    url(r'^questions/(?P<question_id>[0-9]+)/$', question_detailed, name='question_detailed'),
    url(r'^questions/tag/(?P<tag>\w+)/$', questions_by_tag, name='questions_by_tag'),
    url(r'^questions/new/$', new, name='new'),
    url(r'^hot$', hottest, name='hottest_questions'),
    url(r'^guest$', guest, name='guest'),
    url(r'^signin$', signin, name='signin'),
    url(r'^signup$', signup, name='signup'),
    url(r'^parse_request/.*', requestsPrint),
]
