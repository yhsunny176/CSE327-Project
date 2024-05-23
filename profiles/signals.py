from django.db.models.signals import post_save
<<<<<<< Updated upstream
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile

# Create a UserProfile whenever a new User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Save the UserProfile whenever the User is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
=======
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import FreelancerProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        FreelancerProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
>>>>>>> Stashed changes
