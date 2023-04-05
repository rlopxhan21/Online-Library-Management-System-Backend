from rest_framework import serializers

from .models import Author, Genre, Book

class BookViewSerializer(serializers.ModelSerializer):
    patrons = serializers.StringRelatedField(read_only=True)
    genre = serializers.StringRelatedField(read_only=True)
    author = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:
        model = Book
        fields = "__all__"

class BookUpdateSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['status']

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        exclude = ['patrons', 'start_from', 'end_at', 'is_active', 'status']

class GenreSerializer(serializers.ModelSerializer): 
    genre_book_collection = BookViewSerializer(read_only=True, many=True)
    class Meta:
        model = Genre
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):
    author_book_collection = BookViewSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = "__all__"
