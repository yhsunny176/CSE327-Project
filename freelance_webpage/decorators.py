from django.shortcuts import redirect
from django.contrib import messages
from .models import UserProfile

def profile_complete_required(view_func):
    """Decorator for views requiring a complete user profile.

    This decorator ensures that the user's profile is complete before allowing access to the decorated view.
    If the user's profile is incomplete (missing country, street address, or phone number), 
    a warning message is displayed, and the user is redirected to the profile update page.

    :param view_func: The view function to be decorated.
    :type view_func: callable
    :return: The decorated view function.
    :rtype: callable
    """
    def _wrapped_view(request, *args, **kwargs):
        """Checks if the user's profile is complete and redirects if necessary.

        :param request: The HTTP request object.
        :type request: django.http.HttpRequest
        :param args: Additional positional arguments for the view function.
        :param kwargs: Additional keyword arguments for the view function.
        :return: The response from the view function or a redirect to the profile update page.
        :rtype: django.http.HttpResponse
        """
        user_profile = UserProfile.objects.get(user=request.user)
        if not user_profile.country or not user_profile.street_address or not user_profile.phone_number:
            messages.warning(request, "Please complete your profile to continue.")
            return redirect('update_profile')
        return view_func(request, *args, **kwargs)
    return _wrapped_view
