from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
#from django.contrib import flatpages
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jasper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/',include('blog.urls')),
    url(r'^liveupdate/',include('liveupdate.urls')),
    #url(r'^pages/', include(flatpages.urls)),
    #url(r'^media/(?P<path>.*)$','django.contrib.staticfiles.views.serve',{'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )
