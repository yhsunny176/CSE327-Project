from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('freelance_webpage.urls')),
    path('', include('post_project.urls')),
    path('profile/', include('profiles.urls')),  # Add this line
]

