from django.shortcuts import redirect
from django.contrib import messages
from .models import UserProfile

def profile_complete_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        if not user_profile.country or not user_profile.street_address or not user_profile.phone_number:
            messages.warning(request, "Please complete your profile to continue.")
            return redirect('update_profile')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
