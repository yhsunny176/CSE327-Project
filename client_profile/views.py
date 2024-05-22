from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from freelance_webpage.models import UserProfile
from django.contrib import messages

@login_required
def client_profile(request):
    """ Displays the client profile information. This view function renders the client profile page, which contains information
    about the authenticated user's profile. 

    Args:
        request (HttpRequest): The Http Request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered client profile page.
    
    Template:
        'client_profile_info/client-profile.html'
    
    Permissions:
        This view requires the user to be logged in. If the user is not authenticated, they will be redirected
        to the login page
    
    Context:
        No additional context data is passed to the template rendering process.
    """
    return render(request, 'client_profile_info/client-profile.html')


@login_required
def profile_view(request):
    """ Display the user profile informations.This view function retrieves and displays the profile information for the authenticated user.If
    the user is not authenticated, an error message is displayed, and the user is redirected to the login page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The HTTP response object containing the rendered user profile page.
    
    Permissions:
        This view requires the user to be logged in. If the user is not authenticated, they will be redirected
        to the login page.

    Template:
        'client_profile_info/client-profile.html'

    Context:
        - 'user_profile' (UserProfile): The profile information for the authenticated user.
        - 'user_details' (dict): A dictionary containing basic details of the authenticated user,
                                  including first name, last name, date joined, and email.
    """
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)

        # Access user details from the User model
        user_details = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'date_joined': request.user.date_joined,
            'email': request.user.email,
        }

        # Pass data to template context
        context = {
            'user_profile': user_profile,
            'user_details': user_details
        }
        return render(request, 'client_profile_info/client-profile.html', context)
    else:
        # Handle the case when the user is not authenticated
        messages.error(request, "Invalid credentials")
        return redirect(request, 'login')


@login_required
def update_profile(request):
    """ Update the user profile information.This view function allows authenticated users to update their profile information,
    including email address, country, street address, phone number, and profile picture.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponseRedirect: Redirects to the client profile page after successfully updating the profile.
        HttpResponseRedirect: Redirects to the login page if the user is not logged in.

    Permissions:
        This view requires the user to be logged in. If the user is not authenticated, they will be redirected
        to the login page.

    POST Parameters:
        - email (str): The updated email address for the user.
        - country (str): The updated country for the user.
        - street_address (str): The updated street address for the user.
        - phone_number (str): The updated phone number for the user.
        - client_pic_upload (file): The updated profile picture file uploaded by the user.
    """
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        # Get the updated information from the form
        email_address = request.POST.get('email')
        country = request.POST.get('country')
        street_address = request.POST.get('street_address')
        phone = request.POST.get('phone_number')
        client_pic_upload = request.FILES.get('client_pic_upload')

        # Update the user profile information in the database
        if email_address:
            request.user.email = email_address
            request.user.username = email_address
            request.user.save()
            request.session['email_updated'] = True

        if client_pic_upload:
            user_profile.client_pic = client_pic_upload

        if country is not None:
            user_profile.country = country

        if street_address is not None:
            user_profile.street_address = street_address

        if phone is not None:
            user_profile.phone_number = phone

        user_profile.save()

        # Redirect to the profile view page after updating the information
        return redirect('client_profile')
    else:
        messages.error(request, "Sorry, you are not logged in")
        return redirect('login')
