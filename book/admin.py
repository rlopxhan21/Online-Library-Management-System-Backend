from django.contrib import admin

from .models import Author, Genre, Book

admin.site.register(Genre)
admin.site.register(Author)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'genre', 'patrons', "end_at"]
    prepopulated_fields= {"slug": ('name',)}