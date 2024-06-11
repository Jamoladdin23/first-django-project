from django import forms

from books.models import Book


# validaciya, -proveryaet i vidaet error esli ne to piwet, proverka validnosti
def validate_title(value):  # create func i ish value bn
    if value[0].isdigit():  # agar value ni 1 cisi cifr bosa
        raise forms.ValidationError("Book title ne mojet nazivatsya ciframi")  # inoshi owipkani baarasan
        # chtobi et vse rabotala need dobavit ee v class, ukazat s cem work#####3


class BookForm(forms.ModelForm):  # this for work pryamo s modelyami, be worh po parametram i usloviem kak v modele
    # title = forms.Textarea(attrs=)# mojno tak dodavat atributy do vidu field
    title = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validate_title])#####3

    class Meta:
        model = Book
        fields = ['title', 'description', 'cover_image', 'is_published', 'author', 'genre']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'cover_image': forms.FileInput,  # ne imagefield, widget for image is fileinput
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-control'})

        }


