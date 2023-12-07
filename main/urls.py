from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index_page"),
    path("search/", views.search, name="search_results"),
]
