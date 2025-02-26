from django.urls import path

import consult_gpt.consult
from .views import BookListView, AuthorListView, GenreListView, BookCreateView, BookDetailView
import consult_gpt.consult

urlpatterns = [
    path('', BookListView.as_view(), name='books_list'),
    path('author/', AuthorListView.as_view(), name='authors_list'),
    path('books/genres/<int:genre_id>', GenreListView.as_view(), name='genre_detail'),
    path('books/add-book', BookCreateView.as_view(), name='add_book'),
    path('books/<int:pk>', BookDetailView.as_view(), name="book_detail"),
    path('chat_with_gpt/', consult_gpt.consult.chat_with_gpt, name="chat_with_gpt"),
    path('consult/', consult_gpt.consult.consult, name="consult"),
]
