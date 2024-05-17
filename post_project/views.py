from django.shortcuts import render, redirect
from . import models

# Create your views here.
def post_success(request):
    return render(request, "post_project/postsuccess.html") 

def post_project(request):
    if request.method == 'POST':
        pname = request.POST['name']
        category = request.POST['category']
        description = request.POST['description']
        min_price = request.POST['min_price']
        max_price = request.POST['max_price']
        
        attached_file = request.FILES['attached_file']
        
        project =  models.Project(
            project_name=pname,
            category=category,
            project_description=description,
            min_bid_price=min_price,
            max_bid_price=max_price,
            file_doc=attached_file
        )
        
        # Save the project object
        project.save()
        
        return redirect('postsuccess')
        
    return render(request, 'post_project/postproject.html')
