from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from freelance_webpage.models import UserProfile

@login_required
def post_project(request):
    """View function for posting a project.

    This function allows authenticated users to post a new project. It handles POST requests
    containing project details, validates the form data, creates a new project object, and saves
    it to the database. If the request method is GET, it renders the project posting form.

    **Validation and Error Handling:**
    - Ensures `min_price` and `max_price` are numeric.
    - Checks that `min_price` is not greater than `max_price`.
    - Validates the presence of an attached file.

    :param request: The HTTP request object.
    :type request: HttpRequest
    :return: If the request method is POST and the form data is valid, redirects the user to the client projects page. If there are validation errors, renders the project posting form with errors. If the request method is GET, renders the project posting form.
    :rtype: HttpResponse

    :raises ValueError: If `min_price` or `max_price` cannot be converted to an integer.

    :template: post_project/postproject.html
    :context: 
        - min_price (int): The minimum bid price, pre-filled if validation fails.
        - max_price (int): The maximum bid price, pre-filled if validation fails.
        - errors (dict): A dictionary of field-specific error messages.
    """
    if request.method == 'POST':
        pname = request.POST['name']
        category = request.POST['category']
        description = request.POST['description']
        min_price = request.POST['min_price']
        max_price = request.POST['max_price']

        attached_file = request.FILES.get('attached_file')
        
        errors = {}

        # Validate numeric fields
        try:
            min_price = int(min_price)
        except ValueError:
            errors['min_price'] = 'Enter a number.'

        try:
            max_price = int(max_price)
        except ValueError:
            errors['max_price'] = 'Enter a number.'

        if 'min_price' not in errors and 'max_price' not in errors:
            if min_price > max_price:
                errors['min_price'] = 'Minimum price cannot be greater than maximum price.'

        if not attached_file:
            errors['attached_file'] = 'This field is required.'

        if errors:
            return render(request, 'post_project/postproject.html', {
                'min_price': min_price if 'min_price' not in errors else '',
                'max_price': max_price if 'max_price' not in errors else '',
            })

        user_profile = UserProfile.objects.get(user=request.user)

        project = models.Project(
            user=user_profile.user,
            project_name=pname,
            category=category,
            project_description=description,
            min_bid_price=min_price,
            max_bid_price=max_price,
        )

        # Save the project object
        project.save()

        # Save the attached file with its original name
        project.file_doc.save(attached_file.name, attached_file)

        return redirect('clientprojects')
    else:
        return render(request, 'post_project/postproject.html')

