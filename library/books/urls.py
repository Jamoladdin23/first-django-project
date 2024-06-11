#otkrivaetsya a new file py i vse url ccolka perenositsya suda
from django.urls import path

import consult_gpt.consult
from .views import BookListView, AuthorListView, GenreListView, BookCreateView, BookDetailView
import consult_gpt.consult
# tut ot view importuetsya naw new controler

urlpatterns = [
    path('', BookListView.as_view(), name='books_list'),# its will be po default nam dostupniy
    path('author/', AuthorListView.as_view(), name='authors_list'),# as view is funcciya controllera, mojem dodat parametr: napr takoy:extra_context={'title': 'List of authors'}, budet iznacalniy title
    path('books/genres/<int:genre_id>', GenreListView.as_view(), name='genre_detail'), #<int.. is 3 parametr bude prinimat id janru,, cto bi kogda viberiw janry na sayte vidast knigi kotri ye v etom janre
    path('books/add-book', BookCreateView.as_view(), name='add_book'),# first sozdali url fod add book
    path('books/<int:pk>', BookDetailView.as_view(), name="book_detail"),# 'books/<int:book_id>' this for def func views
    path('chat_with_gpt/', consult_gpt.consult.chat_with_gpt, name="chat_with_gpt"),
    path('consult/', consult_gpt.consult.consult, name="consult"),
    # path('', index, name="index"),# tut ne bude books tak kak on est v library urls
    # path("test/", test, name="test")# its be posle books , sozdali ssilku, importuya ot viev
]
