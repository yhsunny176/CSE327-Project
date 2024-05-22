from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Project(models.Model):
    """Model representing a project posted by a user.

    This model stores information about projects posted by users, including the user who posted it,
    project name, category, description, bid price range, attached file (if any), and date posted.

    Attributes:
        user (ForeignKey): The user who posted the project.
        project_name (CharField): The name of the project.
        category (CharField): The category of the project.
        project_description (TextField): The description of the project.
        min_bid_price (PositiveIntegerField): The minimum bid price for the project.
        max_bid_price (PositiveIntegerField): The maximum bid price for the project.
        file_doc (FileField): The attached file for the project (if any).
        posted_on (DateField): The date when the project was posted.

    Methods:
        __str__: Returns the username of the user who posted the project.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    project_description = models.TextField()
    min_bid_price = models.PositiveIntegerField()
    max_bid_price = models.PositiveIntegerField()
    file_doc = models.FileField(upload_to='uploaded_docs/', blank=True, null=True)
    posted_on = models.DateField(default=datetime.date.today, blank=True)

    def __str__(self):
        """Return the username of the user who posted the project.

        :return: The username of the user.
        :rtype: str
        """
        return self.user.username