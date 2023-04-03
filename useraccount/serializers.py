from rest_framework import serializers

from .models import CustomUser
from book.serializers import BookSerialzer

class CustomUserSerializer(serializers.ModelSerializer):
    borrowed_book_collection = BookSerialzer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        exclude = ["password", "groups", 'user_permissions']