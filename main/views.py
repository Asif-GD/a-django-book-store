from json import JSONDecodeError

from django.http import JsonResponse
from rest_framework import status, viewsets
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
    # permission_classes = (IsAuthenticated,)
    # only display books that aren't soft deleted
    queryset = BookList.objects.filter(book_delete_status=False)
    serializer_class = BookListSerializer

    # overriding the destroy() to perform a partial update.
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.book_delete_status = True
        instance.save()
        return Response(data="Soft deletion done. "
                             "To restore the book, access it via the http://127.0.0.1:8000/admin/main/booklist/")
