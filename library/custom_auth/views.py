from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from custom_auth.forms import CustomUserCreateForm, LoginForm


class RegisterViews(CreateView):
    form_class = CustomUserCreateForm
    success_url = reverse_lazy('books_list')
    template_name = 'custom_auth/registration.html'


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)  # tut v form berem dannie
        if form.is_valid():  # tut proveril distvitelnost dnnix
            user = form.get_user()  # tut polucil usera
            login(request, user)
            return redirect('books_list')

    else:
        form = LoginForm()

    return render(request, 'custom_auth/login.html', context={'form': form})


def log_out(request):
    logout(request)
    return redirect('logout')
