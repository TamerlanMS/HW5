from django.urls import path
from . import views

urlpatterns = [
    path('author/', views.AuthorListView.as_view(), name='author_list'),
    path('book/', views.BookListView.as_view(), name='book_list'),
]
