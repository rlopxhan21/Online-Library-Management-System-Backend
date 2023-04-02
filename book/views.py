from rest_framework import mixins, generics, permissions, serializers
from datetime import timedelta
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from .models import Genre, Author, Book
from .serializers import GenreSerializer, AuthorSerializer, BookSerialzer
from .permissons import IsAdminOrReadOnly


class AuthorView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class AuthorDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class GenreView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class GenreDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BookView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialzer
    permission_classes= [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialzer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, reqeust, *args, **kwargs):
        return self.destroy(reqeust, *args, **kwargs)
    
class BookUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerialzer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        pk = self.kwargs['pk']
        book = Book.objects.get(id=pk)

        status = self.request.data.get("status")

        today = timezone.now().date()
        start_from = today

        if status == "R":
            end_at = today + timedelta(2)
        elif status == "B":
            end_at = today + timedelta(21)
        else:
            start_from = None
            end_at = None

        if not self.request.user.is_superuser:
            if Book.objects.filter(end_at__gte=today):
                raise serializers.ValidationError("This book is not available")

        return serializer.save(patrons_id=self.request.user.id, start_from=start_from, end_at=end_at, name=book.name, photo=book.photo, summary=book.summary, releases_time=book.releases_time, is_active=book.is_active, genre=book.genre, slug=book.slug, rating=book.rating)

    def put(self, reqeust, *args, **kwargs):
        return self.update(reqeust, *args, **kwargs)
