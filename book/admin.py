from django.contrib import admin

from .models import Author, Genre, Book

admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Book)
