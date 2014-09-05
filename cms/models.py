from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models import permalink
from markdown import markdown
# Create your models here.

VIEWABLE_STATUS = [3,4]
class ViewableManager(models.Manager):
    def get_query_set(self):
        default_queryset = super(ViewableManager,self).get_query_set()
        return default_queryset.filter(status__in=VIEWABLE_STATUS)

class Category(models.Model):
    """ A content category """
    label = models.CharField(blank=True,max_length=50)
    slug = models.SlugField()
    class Meta:
        verbose_name_plural = "categories"
    def __unicode__(self):
        return self.label

class Story(models.Model):
    """A hunk of content for our site,generally corresponding to a page"""
    STATUS_CHOICES = (
                      (1,"Needs Edit"),
                      (2,"Needs Approval"),
                      (3,"Published"),
                      (4,"Archived"),)
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    category = models.ForeignKey(Category)
    markdown_content = models.TextField()
    html_content = models.TextField(editable=False)
    owner = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES,default=1)
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)
    class Meta:
        ordering = ['modified']
        verbose_name_plural = "stories"
    
    def save(self):
        self.html_content = markdown(self.markdown_content)
        self.modified = datetime.datetime.now()
        super(Story,self).save()
    
    @permalink
    def get_absolute_url(self):
        return ("cms-story",(),{'slug':self.slug})
    
    admin_objects = models.Manager()
    objects = ViewableManager()