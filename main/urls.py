from django.urls import path, include

from . import views as main_views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

router = routers.DefaultRouter()
router.register(r'book', main_views.BookListViewSet, basename='book')
router.register(r'restore-deleted-book', main_views.RestoreSoftDeletedBookViewSet, basename='restore-deleted-book')
urlpatterns = router.urls

urlpatterns += [
    # path("get_all_books/", main_views.get_all_books, name="view_all_books"),
    # path("add_book/", main_views.add_book, name="add_book"),
    # path("restore_book/<book_id>", main_views.restore_book, name="restore_book"),
    path("api-token-auth/", obtain_auth_token),  # gives us access to token auth
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
