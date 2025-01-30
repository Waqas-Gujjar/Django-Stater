from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import redirect , get_object_or_404
from .models import UserProfile
from django.contrib.auth.models import User
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
    if request.path == reverse('profile_onbording'):
        onboarding = True
    else:
        onboarding = False
    return render(request, 'users/profile_edit.html', {'form':form , 'onboarding': onboarding  })

def profile_delete(request, username):
    profile = get_object_or_404(User, username=username).userprofile
    profile.delete()
    messages.success(request, 'Profile deleted successfully')
    return redirect('home')





