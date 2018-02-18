from django.conf.urls import url

from ask.models import *
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
    url(r'^(?P<username>[a-zA-Zа-яА-Я_\-\.0-9]+?)$', profile, name='profile'),
    url(r'^api/question/(?P<pk>\d+)/like/$',
        login_required(VotesView.as_view(model=Question, vote_type=Like.LIKE)),
        name='question_like'),
    url(r'^api/question/(?P<pk>\d+)/dislike/$',
        login_required(VotesView.as_view(model=Question, vote_type=Like.DISLIKE)),
        name='question_dislike'),
    url(r'^api/answer/(?P<pk>\d+)/like/$',
        login_required(VotesView.as_view(model=Answer, vote_type=Like.LIKE)),
        name='answer_like'),
    url(r'^api/answer/(?P<pk>\d+)/dislike/$',
        login_required(VotesView.as_view(model=Answer, vote_type=Like.DISLIKE)),
        name='answer_dislike'),
]
