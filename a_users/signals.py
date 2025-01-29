from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
   user = instance
   if created:
       UserProfile.objects.create(user=user)