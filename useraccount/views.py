from rest_framework import mixins, generics
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomUserSerializer, MyTokenObtainPairSerializer
from .models import CustomUser

class UserView(mixins.ListModelMixin ,generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer