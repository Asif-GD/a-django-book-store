# from json import JSONDecodeError
# from django.http import JsonResponse
from django.http import HttpRequest
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
