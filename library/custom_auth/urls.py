from django.urls import path
from custom_auth.views import RegisterViews, login_view, log_out
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

urlpatterns = [
    path('sign-up/', RegisterViews.as_view(), name="register"),
    path('login/', login_view, name='login'),
    path('logout/', log_out, name='logout')
    # path('logout/', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout')
]
