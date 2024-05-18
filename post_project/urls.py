from django.urls import path
from . import job_views

# Define URL patterns for job-related views
urlpatterns = [
    path('browse-jobs/', job_views.browse_jobs, name='browse_jobs'),  # Browse available jobs
    path('jobs/<int:job_id>/apply/', job_views.apply_job, name='apply_job'),  # Apply for a job by ID
    path('post_job/', job_views.post_job, name='post_job'),  # Post a new job
    path('jobs/my-jobs/', job_views.my_jobs, name='my_jobs'),  # View jobs posted by the current user
    path('jobs/<int:job_id>/details/', job_views.job_details, name='job_details'),  # View job details by ID
    path('jobs/make_submission/<int:application_id>/', job_views.make_submission, name='make_submission'),  # Make a job submission
    path('jobs/aplications/my_applications/', job_views.get_applications, name='get_applications'),  # View applications made by the current user
    path('jobs/submission/recv_submissions/', job_views.recv_submissions, name='recv_submissions'),  # View submissions received for jobs
    path('jobs/submission/accept_submission/<int:submission_id>/', job_views.accept_submission, name='accept_submission'),  # Accept a submission by ID
    path('jobs/submissions/download-file/<int:submission_id>/', job_views.download_file, name='download_file'),  # Download a submitted file by ID
]
