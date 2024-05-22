from django.shortcuts import redirect
from django.contrib import messages
from .models import UserProfile

def profile_complete_required(view_func):
    """Decorator for views requiring a complete user profile.

    This decorator ensures that the user's profile is complete before allowing access to the decorated view.
    If the user's profile is incomplete (missing country, street address, or phone number), 
    a warning message is displayed, and the user is redirected to the profile update page.

    Args:
        view_func (callable): The view function to be decorated.

    Returns:
        callable: The decorated view function.
    """
    def _wrapped_view(request, *args, **kwargs):
        user_profile = UserProfile.objects.get(user=request.user)
        if not user_profile.country or not user_profile.street_address or not user_profile.phone_number:
            messages.warning(request, "Please complete your profile to continue.")
            return redirect('update_profile')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
