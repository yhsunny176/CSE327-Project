from django.urls import include, path
from . import views

urlpatterns = [
    path('client_profile', views.profile_view, name='client_profile'),
    path('client_profile_update', views.update_profile_client, name='client_profile_update')
] 