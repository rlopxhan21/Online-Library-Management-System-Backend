from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

from .views import UserView, MyTokenObtainPairView

urlpatterns = [
    path('jwt/create/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("user-list/", UserView.as_view(), name="user-list")
    ]