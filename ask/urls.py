from django.conf.urls import url

from ask.views import *

app_name = 'ask'
urlpatterns = [
    url(r'^$', newest, name='newest'),
    url(r'^questions/(?P<question_id>[0-9]+)/$', question_detailed, name='question_detailed'),
    url(r'^questions/(?P<question_id>[0-9]+)/write_answer/$', write_answer, name='write_answer'),
    url(r'^questions/tag/(?P<tag_str>.*)/$', questions_by_tag, name='questions_by_tag'),
    url(r'^questions/new/$', new, name='new'),
    url(r'^hot$', hottest, name='hottest_questions'),
    url(r'^signin/.*?$', signin, name='signin'),
    url(r'^signout/.*?$', signout, name='signout'),
    url(r'^signup$', signup, name='signup'),
    url(r'^profile/edit/', settings, name='settings'),
    # url(r'^parse_request/.*', requestsPrint),
]
