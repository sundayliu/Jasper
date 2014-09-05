# -*- coding:utf -*-
# author:sundayliu
# date:2014.9.4
from django.conf.urls import url,patterns
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from models import Story
from django.views.generic.detail import DetailView
from views import category,search

urlpatterns = patterns('',
    url(r'^$',ListView.as_view(model=Story,template_name="story_list.html"),name="cms-home"),
    url(r'^(?P<slug>[-\w]+)/$',DetailView.as_view(model=Story,template_name="story_detail.html"),name="cms-story"),
    url(r'^category/(?P<slug>[-\w]+)/$',category,name="cms-category"),
    url(r'^search/',search,name="cms-search")
    )