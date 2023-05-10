from django.contrib import admin
from .models import Job
from .models import Category
from .models import Form
# Register your models here.

admin.site.register(Job)
admin.site.register(Category)
admin.site.register(Form)
