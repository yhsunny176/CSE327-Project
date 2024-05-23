from django.urls import path
from . import views

app_name = 'profiles'  # Namespace for profiles app

# Define URL patterns for profile views
urlpatterns = [
    path('<int:id>/view/', views.view_profile, name='view_profile'),  # View profile by ID
    path('update/', views.update_profile, name='update_profile'),  # Update profile
    path('update_profile/', views.update_profile, name='update_profile'),
]
