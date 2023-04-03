from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError


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
    slug = models.SlugField(max_length=255)
    photo = models.TextField()
    summary = models.TextField()
    releases_time = models.CharField(max_length=255)
    start_from = models.DateField(null=True, blank=True)
    end_at = models.DateField(null=True, blank=True)
    rating = models.FloatField(default=4, validators=[MinValueValidator(0.1), MaxValueValidator(5)])
    status = models.CharField(max_length=1, default=Status.AVAILABLE, choices=Status.choices)
    is_active = models.BooleanField(default=True)
    
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="genre_book_collection")
    author = models.ManyToManyField(Author, related_name="author_book_collection")
    patrons = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.SET_NULL, related_name="borrowed_book_collection")

    def save(self ,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super().save(*args, **kwargs)

    def clean(self):
        if self.patrons:
            assigned_books_count = Book.objects.filter(patrons=self.patrons).count()

            if assigned_books_count >= 3:
                raise ValidationError("A patron can borrow a maximum of 3 books.")
            
        super().clean()

    def __str__(self) -> str:
        return self.name