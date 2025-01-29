from django import forms
from django.forms import ModelForm
from .models import *

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['display_name', 'image', 'bio', 'location', 'website', 'instagram', 'twitter', 'facebook']
        widgets = {
            'display_name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter': forms.URLInput(attrs={'class': 'form-control'}),
            'facebook': forms.URLInput(attrs={'class': 'form-control'}),    
            }
        labels = {
            'display_name': 'Display Name',
            'image': 'Profile Picture',
            'bio': 'Bio',
            'location': 'Location',
            'website': 'Website',
            'instagram': 'Instagram',
            'twitter': 'Twitter',
            'facebook': 'Facebook',
            }
        error_messages = {
            'display_name': {'required': 'Please enter a display name'},
            'image': {'required': 'Please choose a profile picture'},
            'bio': {'required': 'Please enter a bio'},
            'location': {'required': 'Please enter a location'},
            'website': {'required': 'Please enter a valid website URL'},
            'instagram': {'required': 'Please enter a valid Instagram URL'},
            'twitter': {'required': 'Please enter a valid Twitter URL'},
            'facebook': {'required': 'Please enter a valid Facebook URL'},
            }
        help_texts = {
            'display_name': 'This will be displayed on your profile page',
            'image': 'Choose a profile picture',
            'bio': 'Tell us about yourself',
            'location': 'Where are you located',
            'website': 'Your personal website',
            'instagram': 'Your Instagram profile',
            'twitter': 'Your Twitter profile',
            'facebook': 'Your Facebook profile',
            }
        

