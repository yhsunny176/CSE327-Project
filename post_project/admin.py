from django.contrib import admin
from .models import Project

class PostProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description', 'min_price', 'max_price')


admin.site.register(Project)
