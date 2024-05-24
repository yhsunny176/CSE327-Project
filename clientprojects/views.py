from django.shortcuts import render, redirect

# Create your views here.
def client_projects(request):
    return render(request, 'post_project/clientprojects.html')

