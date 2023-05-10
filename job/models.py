from django.db import models
from django.utils.text import slugify
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
    image = models.ImageField(upload_to=upload_img)
    country = models.CharField(max_length=30)
    
    Responsibility = models.TextField(max_length=2000)
    Qualifications = models.TextField(max_length=1000)
    Benefits = models.TextField(max_length=500)
    
    slug = models.SlugField(blank=True, null=True)
    
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super(Job, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.title
    
    


class Category(models.Model):
    name = models.CharField(max_length=25)
    
    
    def __str__(self) -> str:
        return self.name
    
    

class Form(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    website = models.CharField(max_length=30)
    cv = models.FileField(upload_to='forms/')
    cover_letter = models.TextField(max_length=200)
    filled_at = models.DateTimeField(auto_now=True)
    
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)

    
    def __str__(self):
        return self.name
    