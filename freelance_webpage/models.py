from django.db import models
from django.contrib.auth.models import User
from post_project.models import Project
# Create your models here.
class UserProfile(models.Model):
    USER_ROLES = (
        ('freelancer', 'Freelancer'),
        ('employer', 'Employer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    portfolio = models.OneToOneField('Portfolio', on_delete=models.SET_NULL, null=True, blank=True, related_name='profile')


    

    def __str__(self):
        return self.user.username
    

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional client-specific fields here

    



class Bid(models.Model):
   project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bids')
   
   amount = models.DecimalField(max_digits=10, decimal_places=2)
   message = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)



class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    