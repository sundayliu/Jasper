from django.conf.urls import patterns,url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from models import Paste

display_info = {'queryset':Paste.objects.all()}
create_info = {'model':Paste}

urlpatterns = patterns(
                       '',
                       url(r'^$',ListView.as_view(model=Paste,)),
                       url(r'^(?P<pk>\d+)/$', DetailView.as_view(model=Paste),name="pastebin_detail_url"),
                       url(r'^add/$',CreateView.as_view(model=Paste,)),
                       )