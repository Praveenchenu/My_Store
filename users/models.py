from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pictures',default='profilepic.jpg')
    location = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.user.username

