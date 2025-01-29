from django.urls import path
from .views import *

urlpatterns = [
    path('profile', profile_views, name='profile'),
    path('edit_profile',profile_edit, name='edit_profile'),
]
