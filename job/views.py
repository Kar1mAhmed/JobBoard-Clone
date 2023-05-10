from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .form import FormApply
# Create your views here.

def job_list(request):
    job_list = Job.objects.all()
    
    paginator = Paginator(job_list, 2)
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
        
    else:
        form = FormApply()
    
    context = { 'job' : job,
                'form_data': form
            }
    return render(request, 'job/job_details.html', context)