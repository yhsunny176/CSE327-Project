from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.files.storage import default_storage

@login_required
def view_profile(request, id):
    """
    View a user's profile by ID.
    """
    user = get_object_or_404(User, id=id)
    return render(request, 'profile.html', {'user': request.user, 'target': user})

@login_required
def search_profile(request, name):
    """
    Search for users by name.
    """
    users = User.objects.filter(username__icontains=name)
    return render(request, 'search.html', {'user': request.user, 'search_prompt': name, 'found': users})

@login_required
def get_image(request, user_id):
    """
    Get a user's profile image. Return a default image if not found.
    """
    user = get_object_or_404(User, id=user_id)
    if user.profile.image:
        return HttpResponse(user.profile.image, content_type='image/jpeg')
    else:
        return HttpResponse(default_storage.open('static/Images/default_profile_image.png'), content_type='image/jpeg')
