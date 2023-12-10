from django.urls import path

from . import views

urlpatterns = [
    path("get_all_books/", views.get_all_books, name="view_all_books"),
    path("add_book/", views.add_book, name="add_book"),
]
