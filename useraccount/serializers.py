from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser
from book.serializers import BookViewSerializer

class CustomUserSerializer(serializers.ModelSerializer):
    borrowed_book_collection = BookViewSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        exclude = ["password", "groups", 'user_permissions']

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser
        # ...

        return token
    
