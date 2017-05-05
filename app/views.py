from django.shortcuts import render
from app.models import Book

# Create your views here.

def index_view(request):
    return render(request, template_name="index.html")

def book_list_view(request):
    books = Book.objects.all()
    context = {

    'books' : books
    }
    return render(request, template_name="book_list.html",context=context)
