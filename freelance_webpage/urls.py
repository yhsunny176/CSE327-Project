
from django.contrib import admin
from django.urls import include, path
from freelance_webpage import views
from . import views

urlpatterns = [
path('', views.home, name="home"),
path('register', views.register, name='register'),
path('login', views.login, name='login'), 
path('index', views.login, name='index'),

]
