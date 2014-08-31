from django.conf.urls import patterns, url
from views import archive
from views import index
from views import test
from django.contrib.syndication.views import Feed
from feeds import RSSFeed

urlpatterns = patterns('',
                       # ^ regex start
                       # $ regex end
                       url(r'^$',archive),
                       url(r'^test/$',test),
                       #url(r'^archives/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$',archive)
                       url(r'^feeds/(?P<url>.*)/$',Feed,{'feed_dict':{'rss':RSSFeed}})
                       )