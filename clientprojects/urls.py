from django.urls import include, path
from . import views

urlpatterns = [
    path('clientprojects', views.project_view, name='clientprojects'),
]