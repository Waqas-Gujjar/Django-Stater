from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', profile_views, name='profile'),
    path('@<username>/', profile_views, name='profile'),
    path('edit-profile/',profile_edit, name='edit-profile'),
    path('delete-profile/',profile_delete, name='delete-profile'),
    path('profile-onbording/',profile_edit, name='profile-onboarding'),
    path('profile-settings/',profile_settings, name='profile-settings'),
    path('change-email/', change_email, name='change-email'),
]
