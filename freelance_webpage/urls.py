from django.urls import path
from freelance_webpage import views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'), 
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('post_project/', views.post_project, name='create_project'),
    path('freelancer_dashboard', views.freelancer_dashboard, name='freelancer_dashboard'),
    path('employer_dashboard', views.employer_dashboard, name='employer_dashboard'), 
    path('update_profile/', views.update_profile, name='update_profile'), 
    path('view_projects/', views.view_projects, name='view_projects'),
    path('project_details/<int:project_id>/', views.project_details, name='project_details'),
    path('all_skills/', views.all_skills, name='all_skills'),
    path('skills/create/', views.create_skill, name='create_skill'),
    path('skills/<int:skill_id>/update/',views. update_skill, name='update_skill'),
    path('skills/<int:skill_id>/delete/',views. delete_skill, name='delete_skill'),
    path('create_portfolio/', views.create_portfolio, name='create_portfolio'),
    
]
