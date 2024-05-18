from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

