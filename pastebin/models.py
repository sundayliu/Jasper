from django.db import models
import datetime
from django.db.models import permalink
from django.contrib.sites.models import Site
from django.core.urlresolvers import reverse
# Create your models here.
class Paste(models.Model):
    """ A single pastebin item """
    SYNTAX_CHOICES = {
                      (0,"Plain"),
                      (1,"Python"),
                      (2,"HTML"),
                      (3,"SQL"),
                      (4,"JavaScript"),
                      (5,"CSS"),}
    content = models.TextField()
    title = models.CharField(blank=True,max_length=30)
    syntax = models.IntegerField(max_length=30,choices=SYNTAX_CHOICES,default=0)
    poster = models.CharField(blank=True,max_length=30)
    timestamp = models.DateTimeField(default=datetime.datetime.now,blank=True)
    class Meta:
        ordering = ['-timestamp']
    def __unicode__(self):
        return "%s(%s)" % (self.title or "#%s" % self.id,self.get_syntax_display())
    @permalink
    def get_absolute_url(self):
        #path = reverse('django.views.generic.detail.DetailView.as_view(model=Paste)',None,kwargs = {'pk':self.id})
        #return 'http://%s/pastebin/%s' % (Site.objects.get_current().domain,self.id)
        return ('pastebin_detail_url',(),{'pk':self.id})
        