from rest_framework import mixins, generics, permissions, serializers
from datetime import timedelta
from django.utils import timezone

from .models import Genre, Author, Book
from .serializers import GenreSerializer, AuthorSerializer, BookViewSerializer, BookCreateSerializer, BookUpdateSerialzer
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


class BookView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookViewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class BookCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookCreateSerializer
    permission_classes= [permissions.IsAdminUser]
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookDetailView(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookViewSerializer
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def delete(self, reqeust, *args, **kwargs):
        return self.destroy(reqeust, *args, **kwargs)
    
class BookUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    serializer_class = BookUpdateSerialzer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        slug = self.kwargs['slug']
        return Book.objects.filter(pk=pk, slug=slug)
    
    def perform_update(self, serializer):
        book = self.get_queryset().first()
        status = self.request.data.get("status")

        today = timezone.now().date()
        start_from = today
        patrons_id = self.request.user.id

        if status == "R":
            end_at = today + timedelta(2)
        elif status == "B":
            end_at = today + timedelta(21)
        elif status == "A":
            start_from = None
            end_at = None
            patrons_id = None
        else:
            return serializers.ValidationError("Unknown Status Type.")
                        
        if not self.request.user.is_staff:
            if status == "A" and book.patrons:
                if self.request.user.email != book.patrons.email:
                    raise serializers.ValidationError("You do not have permission to perform this actions.")
                
            elif status == "R" or status =="B":
                if Book.objects.filter(patrons=self.request.user).count() >= 3:
                    raise serializers.ValidationError("You cannot get more than 3 books at a time.")
                if book.end_at:
                    if book.end_at >= today:
                        raise serializers.ValidationError("This book is not available")
        
        return serializer.save(patrons_id=patrons_id, start_from=start_from, end_at=end_at, status=status)

    def put(self, reqeust, *args, **kwargs):
        return self.update(reqeust, *args, **kwargs)
