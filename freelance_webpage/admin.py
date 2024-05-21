from django.contrib import admin
from .models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'user_id', 'country', 'phone_number', 'street_address' )


admin.site.register(UserProfile)