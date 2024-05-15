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
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']

        

    return render(request, "login.html")

def logout(request):
    pass