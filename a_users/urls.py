from django.urls import path
from .views import *

urlpatterns = [
    path('profile', profile_views, name='profile'),
    path('edit-profile',profile_edit, name='edit-profile'),
]
