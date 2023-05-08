from django.contrib import admin
from .models import Job
from .models import Category
# Register your models here.

admin.site.register(Job)
admin.site.register(Category)
