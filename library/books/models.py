from django.db import models
from django.urls import reverse


# Create your models here.
# SOZDAEM CLASS BOOK WILL BE CLASS DLYA TABLICI U NAWEY BDANNIX
# KOROCE TUT SOZDAEM TABLICU

class Author(models.Model):
    first_name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)
    birth_date = models.DateTimeField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="books/profile_images", null=True, blank=True)  # dobavili stolbec image, i upload to kuda zalivaet on image: ponastavili true bo v bz uje est authors poetomu ono ne mojet str dobavit esli ne null
    create_at = models.DateTimeField(auto_now_add=True)  # eto kak default kogda pole sozdavalos
    updated_at = models.DateTimeField(auto_now=True)  # eto prodstavisya kajdiy raz kogda save naw model, kogda pole izmenyalos

    def __str__(self):
        return f"Author: {self.first_name}, {self.last_name}"  # sozdaem chtobi v admine pokazivalo po imeni i fam


class Book(models.Model):  # ot importa unasleduemsya # sozdaem polya, id mojno ne sozdavat, imeetsya defailt # book_id = models.BigAutoField(primary_key=True)# mojno tak dobavit id primary key, a bez nee budet default id
    title = models.CharField(max_length=128)  # sozdali tablicu title s varcharom na 128 symbol
    description = models.TextField(null=True, blank=True)  # null oznacaet wo mojet byt v etoy pole pustoe, blank convertuetsya v adminku, blanc otvecaet proydet li validaciyu na storone django, 99 % idet vmeste 2 true
    cover_image = models.ImageField(upload_to="books/covers")  # mi ukazali kuda ono budet vesti, pit gde mi budem xranit image
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)# part 2 a new strok
    price = models.IntegerField(null=True)# managment comandyq
    rating = models.IntegerField(default=8)# this reyting knigi s defultnim znacenyam


    # this 2 pole created for pri dobavke new rodka do tablici, created ad avtomaticki prostavlyalsya,
    #     koroce kajdiy raz kogda sozdadim new object eto pole budet prostavlyatsya
    create_at = models.DateTimeField(auto_now_add=True)  # eto kak default kogda pole sozdavalos
    updated_at = models.DateTimeField(auto_now=True)  # eto prodstavisya kajdiy raz kogda save naw model, kogda pole izmenyalos

    def get_absolute_url(self):# its for redirecla v CreateViev
        return reverse('book_detail', kwargs={'pk': self.pk})# dobavka ok potomuwo v url book detal trebuet pk

    def __str__(self):
        return f"Book: {self.title}, {self.author}"


class Genre(models.Model):# is foreign for book, paart2
    title = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанри'
        ordering = ['title']# when we do objects.all automatic will sort po title

    def __str__(self):
        return f"Genre: {self.title}"


