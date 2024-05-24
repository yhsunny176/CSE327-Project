from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile,Bid,Skill,Portfolio
from post_project.models import Project


# Create your views here.
def index(request):
    # Clear all messages
    storage = messages.get_messages(request)
    list(storage)  # This will mark all messages as read
    return render(request, "index.html")

def freelancer_dashboard(request):
    return render(request, "dashboards/freelancer-dboard.html")

def employer_dashboard(request):
    return render(request, "dashboards/employer-dboard.html")

def register(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        role = request.POST['role']

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

        user_profile = UserProfile.objects.create(user=myUser, role=role)
        user_profile.save()

        if role == 'freelancer':
            return redirect(reverse('freelancer_dashboard'))
        else:
            return redirect(reverse('employer_dashboard'))
        
    return render(request, "register.html")


def login(request):
    # Clear all messages when rendering the login view
    storage = messages.get_messages(request)
    list(storage)  # This will mark all messages as read

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        messages.info(request, "You are already logged in.")
        if user_profile.role == 'freelancer':
            return redirect('freelancer_dashboard')
        elif user_profile.role == 'employer':
            return redirect('employer_dashboard')
        else:
            return redirect('index')

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or not password:
            messages.error(request, "Please fill out all fields")
            return render(request, "login.html")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            user_profile = UserProfile.objects.get(user=user)
            if user_profile.role == 'freelancer':
                return redirect('freelancer_dashboard')  # Redirect to freelancer dashboard
            elif user_profile.role == 'employer':
                return redirect('employer_dashboard')  # Redirect to employer dashboard
        else:
            messages.error(request, "Invalid credentials")
            return render(request, "login.html")
        if email and password:
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome back, {user.first_name}!")
                return redirect('index')
            else:
                messages.error(request, "Invalid credentials")

    return render(request, "login.html")
    
@login_required
def update_profile(request):
    user = request.user
    user_profile = UserProfile.objects.get(user=user)
    
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        bio = request.POST['bio']
        
        user.first_name = fname
        user.last_name = lname
        user.email = email
        user.save()
        
        user_profile.phone_number = phone_number
        user_profile.bio = bio
        
        if 'profile_picture' in request.FILES:
            user_profile.profile_picture = request.FILES['profile_picture']
        
        user_profile.save()
        
        messages.success(request, "Profile updated successfully")
        return redirect('freelancer_dashboard')
    
    context = {
        'user': user,
        'user_profile': user_profile
    }
    return render(request, 'update_profile.html', context)        



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



def project_details(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    
    if request.method == 'POST':
        amount = request.POST.get('amount')
        message = request.POST.get('message')
        
        if amount and message:
            bid = Bid(
                project=project,
                
                amount=amount,
                message=message
            )
            bid.save()
            
            messages.success(request, 'Your bid has been placed successfully!')
            return redirect('project_details', project_id=project.id)
        else:
            messages.error(request, 'All fields are required.')
    
    return render(request, 'project_details.html', {'project': project})


def all_skills(request):
    skills = Skill.objects.filter(user=request.user)
    return render(request, 'all_skills.html', {'skills': skills})

def create_skill(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            skill = Skill.objects.create(name=name, user=request.user)
            return redirect('all_skills')
    return render(request, 'create_skill.html')

def update_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            skill.name = name
            skill.save()
            return redirect('all_skills')
    return render(request, 'update_skill.html', {'skill': skill})

def delete_skill(request, skill_id):
    skill = get_object_or_404(Skill, id=skill_id)
    if request.method == 'POST':
        skill.delete()
        return redirect('all_skills')
    return render(request, 'delete_skill.html', {'skill': skill})

@login_required
def create_portfolio(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        link = request.POST.get('link')

        portfolio, created = Portfolio.objects.get_or_create(user=request.user, defaults={
            'title': title,
            'description': description,
            'link': link
        })

        if not created:
            portfolio.title = title
            portfolio.description = description
            portfolio.link = link
            portfolio.save()

        user_profile = request.user.userprofile
        user_profile.portfolio = portfolio
        user_profile.save()

        return redirect('freelancer_dashboard')
    return render(request, 'create_portfolio.html')

def logout(request):
    auth_logout(request)
    return redirect('index')
