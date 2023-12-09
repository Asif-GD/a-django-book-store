from rest_framework import serializers

from .models import BookList


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookList
        fields = "__all__"
