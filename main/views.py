# from json import JSONDecodeError
# from django.http import JsonResponse
from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
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


# Create your views here.
# @api_view(["GET"])
# def get_all_books(request):
#     books = BookList.objects.all()
#     serializer = BookListSerializer(books, many=True)
#     return Response(serializer.data)
#
#
# @api_view(["POST"])
# def add_book(request):
#     try:
#         # data = JSONParser().parse(request)
#         serializer = BookListSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     except JSONDecodeError:
#         return JsonResponse({"result": "error", "message": "Json decoding error"}, status=400)


# this is much easier than coding individual views
class BookListViewSet(
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet
):
    """
    A simple ViewSet for listing, retrieving, creating, updating, and soft_deleting books.
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

    # cache implementation
    @method_decorator(cache_page(60 * 60 * 1))  # value in seconds
    # "Authorization" isn't required right now considering IsAuthenticatedOrReadOnly
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
        return Response(data="Soft deletion done. "
                             f"To restore the book, access it via the http://{host}/admin/main/booklist/")

# @api_view(["GET", "PATCH"])
# def restore_book(request, book_id):
#     instance = BookList.objects.filter(id=book_id)
#     instance_data = BookList.objects.filter(id=book_id).values()[0]
#     # book_delete_status = book[0].book_delete_status
#     # book_delete_status = False
#     # title = BookList.objects.filter(id=book_id)[0].title
#     # print(data)
#     print(instance_data)
#     serializer = BookListSerializer(data=instance_data)
#     print(serializer)
#     if serializer.is_valid(raise_exception=True):
#         serializer.restore_book()
#         print(serializer.data)
#         # serializer.book_delete_status = False
#         # serializer.update(instance, serializer.data)
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     # print(book_delete_status, title)
#     # print(type(book))
#     # BookList.restore_book(request)
#     # return Response("Book Restored.")
#
# # @api_view(["GET", "PATCH"])
# # def restore_book(request, book_id):
# #     # instance = BookList.objects.filter(id=book_id)
# #     BookList.restore_book()
# #     return Response("Book Restored.")
