from rest_framework import serializers

from .models import Author, Genre, Book


class BookSerialzer(serializers.ModelSerializer):
    patrons = serializers.StringRelatedField(read_only=True)
    start_from = serializers.DateField(read_only=True)
    end_at = serializers.DateField(read_only=True)
    
    name=serializers.StringRelatedField(read_only=True)
    photo = serializers.StringRelatedField(read_only=True)
    summary = serializers.StringRelatedField(read_only=True)
    releases_time = serializers.StringRelatedField(read_only=True)
    is_active = serializers.StringRelatedField(read_only=True)
    genre = serializers.StringRelatedField(read_only=True)
    author = serializers.StringRelatedField(read_only=True, many=True)
    slug = serializers.StringRelatedField(read_only=True)
    rating = serializers.StringRelatedField(read_only=True)

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
