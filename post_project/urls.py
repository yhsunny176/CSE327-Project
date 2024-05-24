from django.urls import path
from . import views

urlpatterns = [
    path('postproject', views.post_project, name='postproject'),
    path('clientprojects', views.post_success, name='clientprojects'),
    path('view_projects/', views.view_projects, name='view_projects')
]
