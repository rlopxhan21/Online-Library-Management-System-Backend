from django.urls import path

from .views import AuthorView, AuthorDetail, GenreView, GenreDetail, BookView, BookDetail, BookUpdateView

app_name = "book"

urlpatterns =[
    path("author/", AuthorView.as_view(), name="author_list"),
    path('author/<int:pk>/', AuthorDetail.as_view(), name="author-detail"),

    path('genre/', GenreView.as_view(), name="genre_list"),
    path('genre/<int:pk>/', GenreDetail.as_view(), name="genre_detail"),

    path('book/', BookView.as_view(), name="book_list"),
    path('book/<int:pk>/<slug:slug>/', BookDetail.as_view() , name="book_detail"),
    path('book/<int:pk>/<slug:slug>/update/', BookUpdateView.as_view(), name="book_create")
]