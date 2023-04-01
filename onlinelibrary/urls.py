from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("auth/", include("useraccount.urls")),
    path('auth/', include('djoser.urls')),

    path('book/', include('book.urls',namespace='book'))
]
