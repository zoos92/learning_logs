"""Определяет схемы URL для learning_logs."""
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
 # Домашняя страница
	 path('', views.index, name='index'),
 # Страница со списком тем   
     path(r'topics/', views.topics, name='topics'),
 # Страница с подробной информацией по отдельной теме
	 path(r'topics/(<topic_id>\d+)/', views.topic, name='topic'),
 # Страница для добавления новой темы
	 path(r'new_topic/', views.new_topic, name = 'new_topic'),
 # Страница для добавления новой записи
	 path(r'new_entry/(<topic_id>\d+)/', views.new_entry, name = 'new_entry'),
 # Страница для редактирования записи
	 path(r'edit_entry/(<entry_id>\d+)/', views.edit_entry, name = 'edit_entry'),
     path('login/',  LoginView.as_view(template_name='login.html'), name='login'),
     path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
     path('register/', views.register, name='register'),
]