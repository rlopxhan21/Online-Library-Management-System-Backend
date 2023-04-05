from django.urls import path

from .views import AuthorView, AuthorDetail, GenreView, GenreDetail, BookView, BookCreateView, BookDetailView, BookUpdateView

app_name = "book"

urlpatterns =[
    path("author/", AuthorView.as_view(), name="author_list"),
    path('author/<int:pk>/', AuthorDetail.as_view(), name="author-detail"),

    path('genre/', GenreView.as_view(), name="genre_list"),
    path('genre/<int:pk>/', GenreDetail.as_view(), name="genre_detail"),

    path('book/', BookView.as_view(), name="book_list"),
    path('book/create/', BookCreateView.as_view(), name="book_create"),
    path('book/<int:pk>/<slug:slug>/', BookDetailView.as_view() , name="book_detail"),
    path('book/<int:pk>/<slug:slug>/update/', BookUpdateView.as_view(), name="book_create")
]