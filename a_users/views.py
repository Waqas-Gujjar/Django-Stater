from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
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
            # Agar username diya gaya hai toh, us user ka profile fetch karna
            profile = get_object_or_404(User, username=username).userprofile
        else:
            # Agar current logged-in user ka profile fetch karna
            profile = request.user.userprofile
    except ObjectDoesNotExist:
        # Agar user ka profile nahi hai, toh naya profile create karna
        profile = UserProfile.objects.create(user=request.user)  # Naya profile create
        profile.save()  # Save karna profile

    return render(request, 'users/profile.html', {'profile': profile})

@login_required
def profile_edit(request):
    form = UserProfileForm(instance=request.user.userprofile)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile'       )
    return render(request, 'users/profile_edit.html', {'form':form})

def profile_delete(request, username):
    profile = get_object_or_404(User, username=username).userprofile
    profile.delete()
    messages.success(request, 'Profile deleted successfully')
    return redirect('home')





