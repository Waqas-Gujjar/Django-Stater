from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.templatetags.static import static


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    background = models.ImageField(upload_to='background_pics', blank=True)
    displayname = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    



    
    def __str__(self):
        return str(self.user)
    @property
    def name(self):
        if self.displayname:
            name = self.displayname
        else:
            name = self.user.username
        return name
     
    
    
    @property
    def avator(self):
        try:
            avator = self.image.url
        except:
            avator = static('image/avatar.svg')
        return avator
            
    @property
    def banner(self):
        try:
            banner = self.background.url
        except:
            banner = static('image/banner.jpg')
        return banner
            

    
    
   
    
    

    


# Create your models here.
