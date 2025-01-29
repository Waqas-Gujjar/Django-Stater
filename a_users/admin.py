from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'display_name', 'image', 'bio', 'location', 'website', 'instagram', 'twitter', 'facebook']
    search_fields = ['user__username', 'display_name']
    list_filter = ['user__username']
