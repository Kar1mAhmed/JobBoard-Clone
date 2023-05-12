from django.urls import path, include
from .import views

app_name = 'job'

urlpatterns = [  
    path('signup', views.signup, name='signup'),
    path('profile/', views.view_profile, name='profile'),        
    path('profile/edit', views.profile_edit, name='edit_profile'),        
]