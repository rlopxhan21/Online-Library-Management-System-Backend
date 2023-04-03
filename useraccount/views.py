from rest_framework import mixins, generics

from .serializers import CustomUserSerializer
from .models import CustomUser

class UserView(mixins.ListModelMixin ,generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)