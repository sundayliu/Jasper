from django.conf.urls import patterns, url
from models import Update
from django.views.generic import ListView
from liveupdate.views import updates_after

urlpatterns = patterns('',
                       url(r'^$',ListView.as_view(model=Update,)),
                       #url(r'^/after$','django.views.generic.list.ListView'),
                       url(r'^updates-after/(?P<id>\d+)$',updates_after)
                       )