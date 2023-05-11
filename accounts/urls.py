from django.urls import path, include
from .import views

app_name = 'job'

urlpatterns = [  
    path('signup', views.signup, name='signup'),        
]