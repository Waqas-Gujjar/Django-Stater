from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    background = models.ImageField(upload_to='background_pics', blank=True)
    display_name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    website = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)


    
    def __str__(self):
        return str(self.user)
    
    def __str__(self):
        if self.display_name:
            return self.display_name
        else:
            return self.user.username
        
    def avator(self):
        if self.avator:
            return self.image.url
        else:
            return settings.STATIC_URL + 'default_avator.jpg'
            
            

    
    
   
    
    

    


# Create your models here.
