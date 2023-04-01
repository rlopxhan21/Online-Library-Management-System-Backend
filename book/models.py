from django.db import models

from useraccount.models import CustomUser

class Genre(models.Model):
    name= models.CharField(max_length=255)
    about = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Author(models.Model):
    full_name = models.CharField(max_length=255)
    photo = models.TextField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.full_name

class Book(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = 'A', 'AVAILABLE'
        BORROWED = "B", "BORROWED"
        RESERVED = "R", "RESERVED"

    name = models.CharField(max_length=255)
    photo = models.TextField()
    summary = models.TextField()
    releases_time = models.CharField(max_length=255)
    updated = models.DateField(null=True, blank=True)
    booked_till = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, default=Status.AVAILABLE, choices=Status.choices)
    
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="genre_book_collection")
    author = models.ManyToManyField(Author, related_name="author_book_collection")
    patrons = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name="borrowed_book_collection")

    def __str__(self) -> str:
        return self.name