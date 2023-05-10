from django.db import models

# Create your models here.

JOB_TYPES = {
    ('Full Time', 'Full Time'), 
    ('Part Time', 'Part Time')
}

def upload_img(instance, filename):
    _, extension = filename.split('.')
    
    return (f"jobs/{instance.id}.{extension}")

class Job(models.Model):
    title = models.CharField(max_length=100)
    #location = 
    type = models.CharField(max_length=15, choices=JOB_TYPES)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=upload_img)
    country = models.CharField(max_length=30)
    
    Responsibility = models.TextField(max_length=2000)
    Qualifications = models.TextField(max_length=1000)
    Benefits = models.TextField(max_length=500)
    
    slug = models.SlugField(blank=True, null=True)
    
    
    def __str__(self) -> str:
        return self.title
    
    


class Category(models.Model):
    name = models.CharField(max_length=25)
    
    
    def __str__(self) -> str:
        return self.name