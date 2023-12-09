from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import BookList
from .serializers import BookListSerializer


# Create your views here.
@api_view(["GET"])
def get_all_books(request):
    books = BookList.objects.all()
    serializer = BookListSerializer(books, many=True)
    return Response(serializer.data)


def search(response):
    return HttpResponse("<h1>Your search results below.</h1>")
