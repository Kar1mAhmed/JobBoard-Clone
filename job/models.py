from django.db import models

# Create your models here.

JOB_TYPES = {
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time')
}

class Job(models.Model):
    title = models.CharField(max_length=100)
    #location = 
    job_title = models.CharField(max_length=15, choices=JOB_TYPES)
    job_description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    
    
    def __str__(self) -> str:
        return self.title
    
    
    