# from django.urls import path

from . import views as main_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'book', main_views.BookListViewSet, basename='book')
urlpatterns = router.urls

urlpatterns += [
    # path("get_all_books/", views.get_all_books, name="view_all_books"),
    # path("add_book/", views.add_book, name="add_book"),
]
