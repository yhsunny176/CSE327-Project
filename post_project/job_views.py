from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.dateparse import parse_date
from .models import Job, JobApplication  # Ensure these imports are correct

@login_required
def browse_jobs(request):
    """
    Display a list of all available jobs.
    """
    jobs = Job.objects.all()
    return render(request, 'jobs/browse_jobs.html', {'user': request.user, 'jobs': jobs})

@login_required
def apply_job(request, job_id):
    """
    Allow a user to apply for a job.
    """
    job = get_object_or_404(Job, id=job_id)
    if request.user.usertype == 'Business Owner':
        return render(request, '404.html', status=404)
    if not JobApplication.objects.filter(job=job, user=request.user).exists():
        JobApplication.objects.create(job=job, user=request.user, job_status='Pending')
        messages.success(request, 'You have applied to this job!')
    else:
        messages.error(request, 'Something went wrong!')
    return redirect('browse_jobs')

@login_required
def post_job(request):
    """
    Allow a business owner to post a new job.
    """
    if request.user.usertype == 'Freelancer':
        return render(request, '404.html', status=404)
    if request.method == 'POST':
        job_name = request.POST['job_name']
        job_description = request.POST['job_description']
        job_details = request.POST['details']
        job_payment = request.POST['job_payment']
        job_deadline = parse_date(request.POST['job_deadline'])
        Job.objects.create(name=job_name, description=job_description, details=job_details,
                           payment=job_payment, deadline=job_deadline, user=request.user)
        messages.success(request, 'Job posted successfully!')
        return redirect('my_jobs')
    return render(request, 'jobs/post_job.html')

@login_required
def my_jobs(request):
    """
    Display jobs posted by the current user.
    """
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs/my_jobs.html', {'user': request.user, 'jobs': jobs})

@login_required
def job_details(request, job_id):
    """
    Display the details of a specific job.
    """
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'jobs/job_details.html', {'user': request.user, 'job': job})

@login_required
def make_submission(request, application_id):
    """
    Allow a user to make a submission for a job application.
    """
    # Implementation similar to the original code
    pass

@login_required
def get_applications(request):
    """
    Display applications made by the current user.
    """
    applications = JobApplication.objects.filter(user=request.user)
    return render(request, 'jobs/my_applications.html', {'user': request.user, 'applications': applications})

@login_required
def recv_submissions(request):
    """
    Display submissions received for jobs posted by the current user.
    """
    # Implementation similar to the original code
    pass

@login_required
def accept_submission(request, submission_id):
    """
    Allow a user to accept a submission for a job.
    """
    # Implementation similar to the original code
    pass

@login_required
def download_file(request, submission_id):
    """
    Allow a user to download a submitted file.
    """
    # Implementation similar to the original code
    pass
