from django.db import models
from django.contrib import admin
from test.test_imageop import MAX_LEN
from django.db.models.fields.related import ForeignKey
from twisted.conch.insults.insults import modes
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('-timestamp',)
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title','body','timestamp')

class Author(models.Model):
    name = models.CharField(max_length=128)    
class Book(models.Model):
    # CharField
    # TextField
    # EmailField
    # URLField
    # IPAddressField
    # BooleanField : True False
    # NullBooleanField True False None null
    # FileField FilePathField
    # AutoField: default id primary key
    # primary_key = True
    # unique = True
    title = models.CharField(max_length=100)
    # author = models.ForeignKey('Author')
    # author = models.ForeignKey('self')
    # author = models.ForeignKey(Author,related_name='books')
    # author = models.ForeignKey(Author)
    author= models.ManyToManyField(Author,through='AuthorBook')
    length = models.IntegerField()
    
class SmithBook(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author,limit_choices_to = {'name_endswith':'Smith'})
    
class AbstractBook(models.Model):
    title = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    num_pages = models.IntegerField()
    #authors = models.ManyToManyField(Author)
    def __unicode__(self):
        return self.title
    class Meta:
        abstract = True

class TomBook(AbstractBook):
    authors = models.ManyToManyField(Author,limit_choices_to={
                                                              'name_endswith':'Tom'})
class AuthorBook(models.Model):
    collaboration_type = models.CharField(max_length=128)
    book = models.ForeignKey(Book)
    author = models.ForeignKey(Author)
class Game(models.Model):
    game_id = models.IntegerField()
    plat_id = models.IntegerField()
    name = models.CharField(max_length=128)
    cert = models.CharField(max_length=32)
    anti_debug_flag = models.IntegerField()
    anti_debug_gray = models.IntegerField()
    
class Version(models.Model):
    game_id = models.ForeignKey(Game)
    version = models.CharField(max_length=128)
    pkg_fix_crc = models.IntegerField()
    pkg_origin_crc = models.IntegerField()
    main_module = models.CharField(max_length=128)
    cpu1_type = models.IntegerField()
    cpu1_code_size = models.IntegerField()
    cpu1_first_crc = models.IntegerField()
    cpu2_type = models.IntegerField()
    cpu2_code_size = models.IntegerField()
    cpu2_first_crc = models.IntegerField()
class Signature(models.Model):
    game_id = models.ForeignKey(Game)
    version_id = models.ForeignKey(Version)
    sg_name = models.CharField(max_length=16)
    sg_a_crc = models.IntegerField()
    sg_b_crc = models.IntegerField()
    sg_type = models.IntegerField()
    sg_file_type = models.IntegerField()
    sg_status = models.IntegerField()
    sg_gray = models.IntegerField()
    sg_is_delete = models.BooleanField()
    
class Person(models.Model):
    first = models.CharField(max_length=128)
    last = models.CharField(max_length=128)
    middle = models.CharField(max_length=128)
    
    class Meta:
        ordering = ['last','first','middle']
        unique_together = ['first','last','middle']
        
        verbose_name_plural = 'person'
    
admin.site.register(BlogPost, BlogPostAdmin)
