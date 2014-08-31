# -*- coding:utf-8 -*-
'''
Created on 2014.8.31

@author: tata
'''

from django.contrib.syndication.views import Feed
from models import BlogPost

class RSSFeed(Feed):
    title = "Jasper awesome blog feed"
    description = "The latest from my awesome blog"
    link = "/blog/"
    item_link = link
    
    def items(self):
        return BlogPost.objects.all()[:10]