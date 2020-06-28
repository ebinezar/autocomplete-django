"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from books.views import BooksListView, BooksDetailView, BooksCreateView, BooksUpdateView, BooksDeleteView, Autocomplete 

urlpatterns = [
	path('', BooksListView.as_view(), name='books_list'),
    path('books', BooksListView.as_view(), name='books_list'),
	path('books/add', BooksCreateView.as_view(), name='book_add'),
    path('books/detail/<int:pk>', BooksDetailView.as_view(), name='book_detail'),
    path('books/edit/<int:pk>', BooksUpdateView.as_view(), name='book_edit'),
    path('books/delete/<int:pk>', BooksDeleteView.as_view(), name='book_delete'),
	path('books/search', Autocomplete.as_view(), name="book_autocomplete"),
]
