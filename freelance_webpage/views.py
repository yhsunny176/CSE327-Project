from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "index.html")


def register(request):
    # if request.method == "POST":
    #     fname = request.POST['fname']
    #     lname = request.POST['lname']
    #     email = request.POST['email']
    #     phone_number = request.POST['phone_number']
    #     pass1 = request.POST['pass1']
    #     pass2 = request.POST['pass2']

    #     myUser = User.objects.create_user(email, pass1)
    #     myUser.first_name = fname
    #     myUser.last_name = lname

    #     myUser.save()

    #     messages.success(request, "SUCCESSFULLY CREATED")

    #     return redirect('/login')
    
    return render(request, "register.html")




def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['pass1']

        

    return render(request, "login.html")

def logout(request):
    pass