from django.db import models
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """Model representing user profiles.

    This model stores additional information about users, such as their role, country, phone number,
    street address, and profile picture.

    Attributes:
        user (OneToOneField): The associated user instance.
        role (CharField): The role of the user, either 'freelancer' or 'employer'.
        country (CharField): The country of the user.
        phone_number (CharField): The phone number of the user.
        street_address (CharField): The street address of the user.
        client_pic (ImageField): The profile picture of the user.

    Methods:
        __str__: Returns the username of the associated user.
    """
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