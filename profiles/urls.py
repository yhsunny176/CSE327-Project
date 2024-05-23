from django.urls import path
<<<<<<< Updated upstream
from . import profile_views
=======
from . import views
>>>>>>> Stashed changes

app_name = 'profiles'  # Namespace for profiles app

# Define URL patterns for profile views
urlpatterns = [
<<<<<<< Updated upstream
    path('<int:id>/view/', profile_views.view_profile, name='view_profile'),  # View profile by ID
    path('update/', profile_views.update_profile, name='update_profile'),  # Update profile
]
=======
    path('<int:id>/view/', views.view_profile, name='view_profile'),  # View profile by ID
    path('update/', views.update_profile, name='update_profile'),  # Update profile
    path('update_profile/', views.update_profile, name='update_profile'),
]
>>>>>>> Stashed changes
