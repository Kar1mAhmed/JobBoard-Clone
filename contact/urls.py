from django.urls import path
from .import views

app_name = 'contact'

urlpatterns = [  
    path('', views.send_message, name='contact'),        
]