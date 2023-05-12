from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse

from .form import SignupForm, UserEditForm, ProfileEditForm
from .models import Profile
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



def view_profile(request):
    profile = Profile.objects.get(user=request.user) # get the current user object
    context = {'profile': profile}
    return render(request, 'accounts/profile.html', context)



def profile_edit(request):
    profile =  Profile.objects.get(user=request.user)
    
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST,request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            
            user_form.save()
            my_profile = profile_form.save(commit=False)
            
            # Link user with profile
            my_profile.user = request.user
            my_profile.save()
            
            return redirect(reverse("accounts:profile"))
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)
        
    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'accounts/profile_edit.html', context)