from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models

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
        
        project = models.Project(
            project_name=pname,
            category=category,
            project_description=description,
            min_bid_price=min_price,
            max_bid_price=max_price,
            file_doc=attached_file
        )
        
        # Save the project object
        project.save()
        
        return redirect('clientprojects')
    else:
        return render(request, 'post_project/postproject.html')
