from django.views.generic import ListView
from .models import Author, Book

class AuthorListView(ListView):
    model = Author
    template_name = 'appname/author_list.html'

class BookListView(ListView):
    model = Book
    template_name = 'appname/book_list.html'
