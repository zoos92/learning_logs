from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
 
from . import views

urlpatterns = [
    # Страница входа
    path('login/',  LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]