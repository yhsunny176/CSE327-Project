from django.contrib import admin
from .models import Project

class PostProjectAdmin(admin.ModelAdmin):
    """Admin configuration for the Project model.

    This admin class provides configuration options for displaying and interacting with
    Project instances in the Django admin interface.

    Attributes:
        list_display (tuple): The fields to display in the list view of Project instances.
    """
    list_display = ('username','project_name', 'category', 'description', 'min_bid_price', 'max__bid_price', 'file_doc', 'posten_on')


    admin.site.register(Project)
