from django.conf.urls import patterns, url
from views import archive
from views import index
from views import test

urlpatterns = patterns('',
                       # ^ regex start
                       # $ regex end
                       url(r'^$',index),
                       url(r'^test/$',test),
                       url(r'^archives/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',archive)
                       )