from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    avatar = models.ImageField(default='base_profile.png', upload_to='profile_images')
    description = models.TextField(default='기본 자기 소개')

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed