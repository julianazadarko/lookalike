# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Closet(models.Model):
    image = CloudinaryField('image')

class Profile(models.Model):
    #avatar = CloudinaryField('avatar')
    about_me = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    
