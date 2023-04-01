from rest_framework import serializers

from .models import Author, Genre, Book


class BookSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer): 
    genre_book_collection = BookSerialzer(read_only=True, many=True)

    class Meta:
        model = Genre
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    author_book_collection = BookSerialzer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = "__all__"
