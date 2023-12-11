# from rest_framework import status
# from rest_framework.exceptions import APIException
from rest_framework.fields import CharField, IntegerField, BooleanField
from rest_framework_json_api import serializers

from .models import BookList


# class ISBN13IsNotUnique(APIException):
#     status_code = status.HTTP_400_BAD_REQUEST
#     default_detail = "another book with this isbn_13 is already present in the database"
#     default_code = "invalid"


class BookListSerializer(serializers.ModelSerializer):

    title = CharField(required=True)
    book_isbn_13 = IntegerField(required=True)
    book_author = CharField(required=True)
    book_year_of_publication = IntegerField(required=True)
    book_genre = CharField(required=True)
    # stock checking
    book_availability = BooleanField(default=True)
    # soft deletion
    book_delete_status = BooleanField(default=False)

    class Meta:
        model = BookList
        fields = "__all__"
