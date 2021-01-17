  
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print("signal is running")
        new_profile = Profile.objects.create(user=instance)
        new_profile.save()
        print(new_profile)
        print("signal has saved")