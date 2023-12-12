from django.urls import path

from . import views as main_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'book', main_views.BookListViewSet, basename='book')
urlpatterns = router.urls

urlpatterns += [
    # path("get_all_books/", main_views.get_all_books, name="view_all_books"),
    # path("add_book/", main_views.add_book, name="add_book"),
    # path('restore_book/<book_id>', main_views.restore_book, name="restore_book"),
]
