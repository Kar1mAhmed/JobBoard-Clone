from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse

from .models import Job

from .form import FormApply
from .form import FormAdd
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
                'jobs': page_obj,
                'jobs_count' : len(job_list)
            }
    return render(request, 'job/job_list.html', context)


def job_details(request, slug):
    job = Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = FormApply(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()
            return redirect(reverse('jobs:job_list')) # go to job list page after saving

    else:
        form = FormApply()
    
    context = { 'job' : job,
                'form_data': form
            }
    return render(request, 'job/job_details.html', context)



@login_required
def add_job(request):    
    if request.method == 'POST':
        form = FormAdd(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner= request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
        
    else:
        form = FormAdd()
    
    context = {'form_data': form}
    
    return render(request, 'job/add_job.html', context)
