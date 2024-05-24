from django.urls import path
from freelance_webpage import views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'), 
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('freelancer_dashboard', views.freelancer_dashboard, name='freelancer_dashboard'),
    path('employer_dashboard', views.employer_dashboard, name='employer_dashboard'),
]
