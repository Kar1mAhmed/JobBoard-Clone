from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .form import SignupForm
# Create your views here.


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            
            user = authenticate(username=username, password=password)
            login(request, user)
            
            return redirect(reverse('accounts/profile')) # go to job list page after saving

    else:
        form = SignupForm()
    
    context = {'form_data': form}
    
    return render(request, 'registration/signup.html', context)