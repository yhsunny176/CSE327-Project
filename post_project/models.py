from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    project_description = models.TextField()
    min_bid_price = models.PositiveIntegerField()
    max_bid_price = models.PositiveIntegerField()
    file_doc = models.FileField(upload_to='uploaded_docs/', blank=True, null=True)
    posted_on = models.DateField(default=datetime.date.today, blank=True)

    def __str__(self):
        return self.user.username