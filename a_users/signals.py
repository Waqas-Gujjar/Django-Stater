from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from .models import UserProfile

@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
   user = instance
   if created:
       UserProfile.objects.create(user=user)
   else:
       try:
           email_address = EmailAddress.objects.get_primary(user)
           email_address.email = user.email
           email_address.verify = False
           email_address.save()
       except :
          EmailAddress.objects.create(
           user=user,
           email=user.email,
           verified=False, 
           primary=True
          )
           
       

@receiver(pre_save, sender=User)
def presave_user(sender,instance, **kwargs):
    if instance.username:
        instance.username = instance.username.lower()