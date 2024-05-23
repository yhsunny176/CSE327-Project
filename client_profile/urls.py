from django.urls import include, path
from . import views

urlpatterns = [
path('client_profile', views.profile_view, name='client_profile'),
] 