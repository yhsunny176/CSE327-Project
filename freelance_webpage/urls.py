
from django.contrib import admin
from django.urls import include, path
from freelance_webpage import views
from . import views

urlpatterns = [
path('', views.index, name="index"),
path('register', views.register, name='register'),
path('login', views.login, name='login'), 
path('index', views.index, name='index'),

]
