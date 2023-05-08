from django.shortcuts import render
from .models import Job
# Create your views here.

def job_list(requests):
    job_list = Job.objects.all()
    context = {'jobs': job_list}
    return render(requests, 'job/job_list.html', context)


def job_details(requests, id):
    job = Job.objects.get(id=id)
    context = {'job' : job}
    return render(requests, 'job/job_details.html', context)