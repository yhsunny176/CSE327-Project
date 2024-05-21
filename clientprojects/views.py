from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def client_projects(request):
    return render(request, 'post_project/clientprojects.html')

