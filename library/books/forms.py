from django import forms

from books.models import Book


def validate_title(value):
    if value[0].isdigit():
        raise forms.ValidationError("Book title cannot be called by numbers")


class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[validate_title])

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


