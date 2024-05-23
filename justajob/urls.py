"""
URL configuration for justajob project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from freelance_webpage.views import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout, name='logout'),
    path('', include('freelance_webpage.urls')),
    path('', include('post_project.urls')),
    path('', include('clientprojects.urls')),
    path('', include('client_profile.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.CLIENT_PICS_MEDIA_URL, document_root=settings.CLIENT_PICS_MEDIA_ROOT)
    urlpatterns += static(settings.DEFAULT_PICS_MEDIA_URL, document_root=settings.DEFAULT_PICS_MEDIA_ROOT)
    urlpatterns += static(settings.FILE_DOC_MEDIA_URL, document_root=settings.FILE_DOC_MEDIA_ROOT)
