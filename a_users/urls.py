from django.urls import path
from .views import *

urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('@<username>/', profile_view, name='profile'),
    path('edit-profile/',profile_edit_view, name='edit-profile'),
    path('delete-profile/',profile_delete_view, name='delete-profile'),
    path('profile-onbording/',profile_edit_view, name='profile-onboarding'),
    path('profile-settings/',profile_settings_view, name='profile-settings'),
    path('confirm-email/', profile_settings_view, name='confirm-email'),  # confirm email after signup
    path('change-email/', profile_emailchange, name='change-email'),
]
