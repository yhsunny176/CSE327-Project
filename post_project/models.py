from django.db import models

# Create your models here.
class Project(models.Model):
    project_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    project_description = models.TextField()
    min_bid_price = models.PositiveIntegerField()
    max_bid_price = models.PositiveIntegerField()
    file_doc = models.FileField(upload_to='uploaded_docs/', blank=True, null=True)
