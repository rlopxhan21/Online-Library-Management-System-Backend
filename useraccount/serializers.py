from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser
from book.serializers import BookSerialzer

class CustomUserSerializer(serializers.ModelSerializer):
    borrowed_book_collection = BookSerialzer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        exclude = ["password", "groups", 'user_permissions']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # ...

        return token
    
