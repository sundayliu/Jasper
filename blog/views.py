from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
from blog.models import BlogPost
from blog.models import Book
from blog.models import Author
# Create your views here.

def archive(request,year,month,day):
    posts = BlogPost.objects.all()
    t = loader.get_template('archive.html')
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))

def index(request):
    response = HttpResponse()
    response.write("<html>")
    response.write("This is a tiny index page!")
    response.write("</html>")
    return response

def test(request):
    response = HttpResponse()
    response.write("<html>")
    response.write("This is a tiny test page!")
    response.write("</html>")
    return response

def books(request):
    book = Book.objects.get(title='Python Web Development Django')
    authors = book.author_set.all()
    books = authors[2].book_set.all()
