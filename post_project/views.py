from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project


@login_required
def post_success(request):
    user = request.user
    return render(request, "post_project/clientprojects.html", {'user': user}) 

@login_required
def post_project(request):
    if request.method == 'POST':
        pname = request.POST['name']
        category = request.POST['category']
        description = request.POST['description']
        min_price = request.POST['min_price']
        max_price = request.POST['max_price']
        
        attached_file = request.FILES['attached_file']

        
         
          
        
        Project.objects.create(
             project_name=pname,
            category=category,
            project_description=description,
            min_bid_price=min_price,
            max_bid_price=max_price,
            file_doc=attached_file
        )
        
        
       
        
        return redirect('clientprojects')
    else:
        return render(request, 'post_project/postproject.html')
    
@login_required
def view_projects(request):
    query = request.GET.get('q')
    if query:
        projects = Project.objects.filter(
            project_name__icontains=query
        ) | Project.objects.filter(
            category__icontains=query
        ) | Project.objects.filter(
            project_description__icontains=query
        )
    else:
        projects = Project.objects.all()
    return render(request, 'view_projects.html', {'projects': projects, 'query': query})

    
