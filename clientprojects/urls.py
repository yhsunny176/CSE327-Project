from django.urls import include, path
from . import views

urlpatterns = [
path('clientprojects', views.client_projects, name='clientprojects'),
]