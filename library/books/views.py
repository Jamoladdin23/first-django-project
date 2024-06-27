from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView

from books.forms import BookForm
from books.models import Author, Book, Genre


class AuthorListView(ListView):
    model = Author
    extra_context = {
        'title': 'List of authors'}


class BookListView(ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        query = super().get_queryset()
        return query.select_related('author', 'genre')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genres'] = Genre.objects.all()
        return context


class GenreListView(ListView):
    model = Genre
    template_name = 'books/genre.html'
    context_object_name = 'books'

    def get_queryset(self):
        books = Book.objects.filter(
            genre__id=self.kwargs['genre_id'])
        return books

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = get_object_or_404(Genre, pk=self.kwargs['genre_id'])
        context['genres'] = Genre.objects.all()

        return context


class BookCreateView(CreateView):
    form_class = BookForm
    template_name = 'books/create_book.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'

