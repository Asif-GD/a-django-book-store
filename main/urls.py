from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_all_books, name="landing_page"),
    path("add_book/", views.add_book, name="add_book"),
]
