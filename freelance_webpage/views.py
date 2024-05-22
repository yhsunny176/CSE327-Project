from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import UserProfile

# Create your views here.
def index(request):
    """Renders the index page.

    This view function renders the index page of the website.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object containing the rendered index page.
    :rtype: HttpResponse
    """
    return render(request, "index.html")


def freelancer_dashboard(request):
    """Renders the freelancer dashboard page.

    This view function renders the dashboard page for freelancers.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object containing the rendered freelancer dashboard page.
    :rtype: HttpResponse
    """
    return render(request, "dashboards/freelancer-dboard.html")


def employer_dashboard(request):
    """Render the employer dashboard page.

    This view function renders the dashboard page for employers.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object containing the rendered employer dashboard page.
    :rtype: HttpResponse
    """
    return render(request, "dashboards/employer-dboard.html")


def register(request):
    """Handle user registration.

    This view function handles user registration. It validates the submitted form data,
    creates a new user account, logs in the user, and redirects them to the appropriate dashboard.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object containing the rendered registration page or a redirect to the dashboard.
    :rtype: HttpResponse
    """
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone_number']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        role = request.POST['role']

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, "register.html")

        myUser = User.objects.create_user(
            username=email, email=email, password=pass1)
        myUser.first_name = fname
        myUser.last_name = lname
        myUser.save()

        user_profile = UserProfile.objects.create(
            user=myUser, role=role, phone_number=phone)

        if not user_profile.country:
            user_profile.country = 'Update Your Country'
        if not user_profile.street_address:
            user_profile.street_address = 'Update Your Street Address'
        if not user_profile.client_pic:
            user_profile.client_pic = 'default_pics/p2.png'
        user_profile.save()

        # Automatically log in the user after registration
        auth_login(request, myUser)

        if role == 'freelancer':
            return redirect('freelancer_dashboard')
        else:
            return redirect('employer_dashboard')

    return render(request, "register.html")


def login(request):
    """Handle user login.

    This view function handles user login. It validates the submitted credentials,
    authenticates the user, logs in the user, and redirects them to the appropriate dashboard.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object containing the rendered login page or a redirect to the dashboard.
    :rtype: HttpResponse
    """
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        messages.info(request, "You are already logged in.")
        if user_profile.role == 'freelancer':
            return redirect('freelancer_dashboard')
        elif user_profile.role == 'employer':
            return redirect('employer_dashboard')
        else:
            return redirect('index')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Please fill out all fields")
            return render(request, "login.html")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            user_profile = UserProfile.objects.get(user=user)
            if user_profile.role == 'freelancer':
                return redirect('freelancer_dashboard')
            elif user_profile.role == 'employer':
                return redirect('employer_dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login.html")

    return render(request, "login.html")


@login_required
def logout(request):
    """Handle user logout.

    This view function handles user logout. It logs out the currently authenticated user and
    redirects them to the index page.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: Redirects to the index page after successfully logging out.
    :rtype: HttpResponseRedirect
    
    :permission: This view requires the user to be logged in. If the user is not authenticated, they will be redirected
                 to the index page
    """
    auth_logout(request)
    return redirect('login')
