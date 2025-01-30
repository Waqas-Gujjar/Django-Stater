from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, ChangeEmailForm
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect , get_object_or_404
from .models import UserProfile 
from django.contrib.auth.models import User
from django.contrib.auth import  login, logout
from allauth.account.utils import send_email_confirmation
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import ObjectDoesNotExist

@login_required
def profile_views(request, username=None):
    try:
        if username:
            
            profile = get_object_or_404(User, username=username)
        else:
            
            profile = request.user.userprofile 
    except ObjectDoesNotExist:
        profile = UserProfile.objects.create(user=request.user)  # Naya profile create
        profile.save()  

    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    form = UserProfileForm(instance=request.user.userprofile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
        
    if request.path == reverse('profile-onboarding'):
        onboarding = True
    else:
        onboarding = False
    return render(request, 'users/profile_edit.html', {'form':form , 'onboarding': onboarding  })

def profile_settings(request):
    return render(request, 'users/profile_setting.html')

@login_required
def profile_delete(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Profile deleted successfully')
        return redirect('account_signup')
    return render(request, 'users/profile_delete.html')

def change_email(request):
    if request.htmx:
        form = ChangeEmailForm( instance=request.user)
        return render(request, 'partials/change_email.html',{'form':form})
    if request.method == 'POST':
        form = ChangeEmailForm(request.POST, instance=request.user)
        if form.is_valid():
             email = form.cleaned_data['email']
             if User.objects.filter(email=email).exclude(id=request.user.id).exists():
                    messages.error(request, 'Email already exists')
                    return redirect('profile-settings')
             form.save()
             send_email_confirmation(request, request.user)
             return redirect('profile-settings')
        else:
            messages.error(request, 'Invalid email')
            return redirect('profile-settings')
    return redirect('home')






