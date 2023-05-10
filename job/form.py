from django import forms

from .models import Form


class FormApply(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name', 'email', 'website', 'cv', 'cover_letter'] # what are visible in form