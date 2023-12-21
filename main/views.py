from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.mixins import (
    ListModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin
)

from .models import BookList
from .serializers import BookListSerializer


# this is much easier than coding individual views
class BookListViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet):
    """
    A simple ViewSet for listing, retrieving, creating, updating, and soft deleting books.
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # only display books that aren't soft deleted
    queryset = BookList.objects.filter(book_delete_status=False)
    serializer_class = BookListSerializer

    # cache implementation
    @method_decorator(cache_page(60 * 60 * 1))  # value in seconds
    # "Authorization" isn't required right now considering IsAuthenticatedOrReadOnly
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(cache_page(60 * 60 * 1))  # value in seconds
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # overriding the destroy() to perform a partial update.
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.book_delete_status = True
        instance.save()
        host = HttpRequest.get_host(request)
        book_id = instance.id
        return Response(status=status.HTTP_200_OK,
                        data=f"Soft deletion done. "
                             f"To restore the book, access it via http://{host}/restore-deleted-book/{book_id}/")


class RestoreSoftDeletedBookViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    viewsets.GenericViewSet):
    """
    A simple ViewSet to restore soft deleted books.
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = BookListSerializer
    # only display books that are soft deleted
    queryset = BookList.objects.filter(book_delete_status=True)

    @method_decorator(cache_page(60 * 60 * 1))  # value in seconds
    # "Authorization" isn't required right now considering IsAuthenticated
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @method_decorator(cache_page(60 * 60 * 1))  # value in seconds
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()
        instance.book_delete_status = False
        instance.save()
        # self.update(request, *args, **kwargs)
        host = HttpRequest.get_host(request)
        book_id = instance.id
        return Response(status=status.HTTP_200_OK,
                        data=f"Book restored. "
                             f"To view the book, access it via http://{host}/book/{book_id}/")
