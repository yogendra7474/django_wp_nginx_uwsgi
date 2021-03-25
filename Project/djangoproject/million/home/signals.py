from django.db.models.signals import post_save
from django.contrib.auth.signals import user_logged_in

from accounts.models import User
from .models import Profile, UserCredit
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_UserCredit(sender, instance, created, **kwargs):
    if created:
        UserCredit.objects.create(user=instance)




# user_logged_in.connect(log, sender=User)  
