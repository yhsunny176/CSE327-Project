from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def index(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

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

        messages.success(request, "Successfully created")
        return redirect('index')

    return render(request, "register.html")




def login(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
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
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect('index')
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login.html")

    return render(request, "login.html")
        

def logout(request):
    auth_logout(request)
    return redirect('index')
