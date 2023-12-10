from json import JSONDecodeError

from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import BookList
from .serializers import BookListSerializer


# Create your views here.
@api_view(["GET"])
def get_all_books(request):
    books = BookList.objects.all()
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def add_book(request):
    try:
        # data = JSONParser().parse(request)
        serializer = BookListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except JSONDecodeError:
        return JsonResponse({"result": "error", "message": "Json decoding error"}, status=400)
