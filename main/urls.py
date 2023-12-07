from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home_page"),
    path("search/", views.search, name="search_results"),
]