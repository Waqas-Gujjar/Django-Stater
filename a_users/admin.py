from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'displayname', 'image', 'bio', 'location', 'website', 'instagram', 'twitter', 'facebook']
    search_fields = ['user__username', 'displayname']
    list_filter = ['user__username']
