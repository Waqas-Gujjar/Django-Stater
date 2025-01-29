from django.urls import path
from .views import *

urlpatterns = [
    path('profile', profile_views, name='profile'),
]
