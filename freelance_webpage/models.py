from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    USER_ROLES = (
        ('freelancer', 'Freelancer'),
        ('employer', 'Employer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES)
    country = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    client_pic = models.ImageField(upload_to='client_pics/', null=True, blank=True)

    def __str__(self):
        return self.user.username