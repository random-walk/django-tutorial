__author__ = 'genmasuda'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # ?P<question_id> is the argument that will hold the value captured by the regex grouping
    # /polls/12/ -> calls views.detail(request=<HttpRequest object>, question_id=12)
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

