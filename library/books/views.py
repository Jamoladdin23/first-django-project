# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect  # its popular func for rendera: importuem i sozdaem norm model html file, otkrivaya iznacalno directorii templates and books
from django.views.generic import ListView, DetailView, CreateView

from books.forms import BookForm
from books.models import Author, Book, Genre


# nojno otrimat autorov ili janrov cbv class best view

class AuthorListView(ListView):
    model = Author
    extra_context = {
        'title': 'List of authors'}  # ili mojno ee suda zapisat v per , vse tak je rabotaet no toje ne practicno recomended kogda mi ststicni dasnni peredaem vnutri {}
    # template_name = 'books/author_list.html'   # its for specify konkret html adres na kakom ono budet


# def authors_list(request):
#     authors = Author.objects.all()
#     context = {'authors': authors,
#                'title': 'List of authors'}  # is slovar v kotorom budet vse neobxidni nawi peremennie
#     return render(request, 'books/author_list.html',
#                   context)  # first request, potom imya template- shablona, potom qontext
# ---------------------------
class BookListView(ListView):
    model = Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):# sozdali this func co bi udelat menwe bilo zaprosov
        query = super().get_queryset()
        return query.select_related('author', 'genre')# cerez select related

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # call s super i. xranim v context
        context['genres'] = Genre.objects.all()  # peredaem te zminni kaloe treba, genres
        return context


# def books_list(request):
#     books = Book.objects.all()
#     genres = Genre.objects.all()  # tut uje nado otobrojat i knigi i spisok janriv
#     context = {
#         'books': books,
#         'genres': genres
#     }
#     return render(request, 'books/books_list.html', context)
# --------------------------
class GenreListView(ListView):
    model = Genre  # povertaem vse ganry
    template_name = 'books/genre.html'
    context_object_name = 'books'

    def get_queryset(self):
        books = Book.objects.filter(
            genre__id=self.kwargs['genre_id'])  # return filtrovanniy query po genre id, v kwargs popadaet vse dannie
        return books

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = get_object_or_404(Genre, pk=self.kwargs['genre_id'])  # obrabotka try except
        context['genres'] = Genre.objects.all()

        return context


# def genre_detail(request, genre_id):  # 2 param is for naxodki ego v template janr iz url
# books = Book.objects.filter(genre__id=genre_id)  # for sort po indexu
# genres = Genre.objects.all()
# try:
#     genre = Genre.objects.get(
#         pk=genre_id)  # vidast owibku exist, if malo, if mnogo to multiply, poetomu mi obrabotaem ego
# except Genre.DoesNotExist:
#     return HttpResponseNotFound()
#
# context = {
#     'books': books,
#     'genres': genres,
#     'genre': genre
# }
# return render(request, 'books/genre.html', context)

# -------------------------
# def add_book(request):  # potom create wiev and importuvali v url i potom template
#     if request.method == 'POST':  # agar status is post
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():  # proveryaem vse dannie sxoditsya to
#             print(form.cleaned_data)  # tut polucaem skonvertovaniy znachenya s typiv dannix,,
#             book = form.save()  # this for 2 method
#             # book = Book.objects.create(**form.cleaned_data)#tut rozpakuem dannie knigi, zapis knig this for 1 varik
#             return redirect('book_detail', book_id=book.pk)  # redirect tekuwis stranicu na drugu, only need import
#     else:
#         form = BookForm()
#     return render(request, 'books/create_book.html',
#                   {'form': form})  # this reurn pod else doljno bit chto bi ostavalsta v toy je page

class BookCreateView(CreateView):
    form_class = BookForm
    template_name = 'books/create_book.html'

#---------------------------

# def book_detail(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     context = {"book": book}
#     return render(request, "books/book_detail.html", context)


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'




#------------------------------------------



# eto vse prosto primer s vivodom na ekran textom
# def index(request):  # sozdaem funcciyu
#     return HttpResponse('hello world')  # vivodim default dlya nawego django application
#
#
# def test(request):  # sozdaem new controller test
#   return HttpResponse("<h1>test title</h1>")

