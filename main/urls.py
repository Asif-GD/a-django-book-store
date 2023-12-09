from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_all_books, name="landing_page"),
    path("search/", views.search, name="search_results"),
]
