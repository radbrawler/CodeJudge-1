from django.conf.urls import patterns, url
from judge.views import * 

urlpatterns = patterns('',
	url(r'^$', IndexView.as_view(), name='index'),
)