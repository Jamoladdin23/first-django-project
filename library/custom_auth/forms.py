# tut sozdaem formu dlya registracii usera

from django import forms  # its for castomizace, polucaetsya castomiziruem s form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # its need tpo import
from django.contrib.auth.models import User  # its default user


class CustomUserCreateForm(UserCreationForm):  # sozdaem clas formi kak ono budet pitat reg
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # teper need to create views


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
