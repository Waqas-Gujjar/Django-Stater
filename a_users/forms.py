from django import forms
from django.forms import ModelForm
from .models import *

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['displayname', 'image', 'bio', 'location']
        widgets = {
            'displayname': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),   
            }
        help_texts = {
            'displayname': 'Display Name',
            'image': 'Profile Picture',
            'bio': 'Bio',
            'location': 'Location',

            }
        

