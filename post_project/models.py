from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    """
    Model representing a job posted by a user.
    """
    name = models.CharField(max_length=255)  # Job name
    description = models.TextField()  # Job description
    details = models.TextField()  # Additional job details
    payment = models.DecimalField(max_digits=10, decimal_places=2)  # Payment amount
    deadline = models.DateField()  # Application deadline
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User who posted the job

    def __str__(self):
        return self.name  # String representation of the job

class JobApplication(models.Model):
    """
    Model representing a job application by a user.
    """
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')  # Job being applied for
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User applying for the job
    job_status = models.CharField(max_length=50, default='Pending')  # Status of the application

    def __str__(self):
        return f"{self.user.username} - {self.job.name}"  # String representation of the application
