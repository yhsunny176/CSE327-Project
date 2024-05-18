from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from .models import UserProfile


# Create your views here.
def index(request):
    return render(request, "index.html")

def freelancer_dashboard(request):
    return render(request, "dashboards/freelancer-dboard.html")

def employer_dashboard(request):
    return render(request, "dashboards/employer-dboard.html")


def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        role = request.POST['role']

        if pass1 != pass2:
            messages.error(request, "Passwords do not match")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, "register.html")

        myUser = User.objects.create_user(username=email, email=email, password=pass1)
        myUser.first_name = fname
        myUser.last_name = lname
        myUser.save()

        user_profile = UserProfile.objects.create(user=myUser, role=role)
        user_profile.save()

        if role == 'freelancer':
            return redirect(reverse('freelancer_dashboard'))
        else:
            return redirect(reverse('employer_dashboard'))
        
    return render(request, "register.html")


def login(request):
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
                return redirect('freelancer_dashboard')  # Redirect to freelancer dashboard
            elif user_profile.role == 'employer':
                return redirect('employer_dashboard')  # Redirect to employer dashboard
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login.html")

    return render(request, "login.html")
        

def logout(request):
    auth_logout(request)
    return redirect('index')
