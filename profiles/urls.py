from django.urls import path
from . import profile_views

# Define URL patterns for profile views
urlpatterns = [
    path('<int:id>/view/', profile_views.view_profile, name='view_profile'),  # View profile by ID
    path('search/<str:name>/', profile_views.search_profile, name='search_profile'),  # Search profile by name
    path('users/<int:user_id>/get-image/', profile_views.get_image, name='get_image'),  # Get user profile image
]
