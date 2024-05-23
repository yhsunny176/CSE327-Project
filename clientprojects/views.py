from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from freelance_webpage.models import UserProfile
from django.contrib import messages
from post_project.models import Project
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def project_view(request):
    """Displays the projects associated with the authenticated user.

    This view function retrieves and displays the projects associated with the authenticated user's profile.
    If the user is not authenticated, an error message is displayed, and the user is redirected to the login page.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: The HTTP response object containing the rendered projects page.
    :rtype: HttpResponse

    :permission: This view requires the user to be logged in. If the user is not authenticated, they will be redirected
                 to the login page.
                 
    :context:
        - user_profile (UserProfile): The profile information for the authenticated user.
        - user_details (dict): A dictionary containing the first name and last name of the authenticated user.
        - project_details (QuerySet): The projects associated with the authenticated user.
        - page_obj (Paginator.page): The current page of projects, used for pagination..
    """
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)

        project_details = Project.objects.filter(user=request.user)
        
        # Pagination setup
        paginator = Paginator(project_details, 9)  # Show 9 projects per page
        page_number = request.GET.get('page')
        try:
            page_obj = paginator.page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

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
            'page_obj': page_obj,
        }
        return render(request, 'post_project/clientprojects.html', context)
    else:
        # Handle the case when the user is not authenticated
        messages.error(request, "Invalid credentials")
        return redirect(request, 'login')