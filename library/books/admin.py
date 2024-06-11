from django.contrib import admin

# Register your models here.
from books.models import Author, Book, Genre #do import classov modeley dlya to wob work cerez adminku

admin.site.register(Author)# here mi nastroili nawu adminku
admin.site.register(Book)
admin.site.register(Genre)