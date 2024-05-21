from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from freelance_webpage.models import UserProfile
from post_project.models import Project
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def post_project(request):
    if request.method == 'POST':
        pname = request.POST['name']
        category = request.POST['category']
        description = request.POST['description']
        min_price = request.POST['min_price']
        max_price = request.POST['max_price']

        attached_file = request.FILES['attached_file']

        user_profile = UserProfile.objects.get(user=request.user)

        project = models.Project(
            user=user_profile.user,
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


@login_required
def project_view(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)

        project_details = Project.objects.filter(user=request.user)

        # Pagination logic
        paginator = Paginator(project_details, 9)  # Show 9 projects per page
        page = request.GET.get('page')

        try:
            projects = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            projects = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            projects = paginator.page(paginator.num_pages)

        # Access user details from the User model
        user_details = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }

        # Pass data to template context
        context = {
            'user_profile': user_profile,
            'user_details': user_details,
            'project_details': project_details,
            'projects': projects,
        }
        return render(request, 'post_project/clientprojects.html', context)
    else:
        # Handle the case when the user is not authenticated
        messages.error(request, "Invalid credentials")
        return redirect(request, 'login')
