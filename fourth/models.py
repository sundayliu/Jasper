from django.db import models
from django.contrib import admin

# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    
class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
                 ("Name",{"fields":("firstname","lastname")}),
                 ("Location",{"fields":("city","state")})
                 ]
admin.site.register(Person, PersonAdmin)