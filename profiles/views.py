from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.core.files.storage import default_storage
from .forms import ProfileForm
from .models import FreelancerProfile

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

@login_required
def update_profile(request):
    user_profile, created = FreelancerProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)
    return render(request, 'profiles/update_profile.html', {'form': form})
