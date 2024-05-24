from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    """Admin configuration for the UserProfile model.

    This admin class provides configuration options for displaying and interacting with
    UserProfile instances in the Django admin interface.

    Attributes:
        list_display (tuple): The fields to display in the list view of UserProfile instances.
    """
    list_display = ('id', 'role', 'user_id', 'country', 'phone_number', 'street_address' )


admin.site.register(UserProfile)