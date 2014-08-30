'''
Created on 2014.8.30

@author: tata
'''
from django import forms
from models import Person


class LargeTextareaWidget(forms.Widget):
    def __init__(self,*args,**kwargs):
        kwargs.setdefault('attrs',{}).update({'rows':40,'cols':100})
        super(LargeTextareaWidget,self).__init__(*args,**kwargs)

class ContentForm(forms.Form):
    name = forms.CharField()
    markup = forms.ChoiceField(choices=[
                                        ('markdown','Markdown'),
                                        ('textile','Textile')])
    text = forms.Textarea(widget=LargeTextareaWidget)
class PersonForm(forms.Form):
    first = forms.CharField(max_length=128,required=True)
    last = forms.CharField(max_length=128,required=True)
    middle = forms.CharField(max_length=128)
    

class Person1Form(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ('middle',)

class Person2Form(forms.ModelForm):
    class Meta:
        model =Person
        fields = ('first','last')
class Person3Form(forms.ModelForm):
    first = forms.CharField(max_length=16)
    class Meta:
        model = Person