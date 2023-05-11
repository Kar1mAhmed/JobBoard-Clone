from django import forms

from .models import Form
from .models import Job


class FormApply(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'email', 'website', 'cv', 'cover_letter'] # what are visible in form
        
        

class FormAdd(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('published_at', 'slug', 'owner')