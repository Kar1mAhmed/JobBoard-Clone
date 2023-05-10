from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    
    paginator = Paginator(job_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
                'jobs': page_obj,
                'jobs_count' : len(job_list)
            }
    return render(request, 'job/job_list.html', context)


def job_details(requests, id):
    job = Job.objects.get(id=id)
    context = {'job' : job}
    return render(requests, 'job/job_details.html', context)