from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
path('postproject', views.post_project, name='postproject'),
]