from django.db import models
from django.contrib.auth.models import User

# Define UserProfile model to store additional user information
<<<<<<< Updated upstream
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to Django User model
=======
class FreelancerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # Link to Django User model
>>>>>>> Stashed changes
    age = models.IntegerField(blank=True, null=True)  # Age field
    address = models.CharField(max_length=255, blank=True)  # Address field
    skills = models.CharField(max_length=255, blank=True)  # Skills field
    description = models.TextField(blank=True)  # Description field
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)  # Profile image field

    def __str__(self):
<<<<<<< Updated upstream
        return self.user.username  # String representation
=======
        return self.user.username  # String representation
>>>>>>> Stashed changes
