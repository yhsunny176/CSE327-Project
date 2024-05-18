from django.urls import path
from . import profile_views

app_name = 'profiles'  # Namespace for profiles app

# Define URL patterns for profile views
urlpatterns = [
    path('<int:id>/view/', profile_views.view_profile, name='view_profile'),  # View profile by ID
    path('update/', profile_views.update_profile, name='update_profile'),  # Update profile
]
