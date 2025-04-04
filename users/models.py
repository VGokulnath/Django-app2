from django.db import models

from django.contrib.auth.models import User    # 1 user going to have 1 profile


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)  #if the user is deleted profile of that user should also delete
    image = models.ImageField(default='profilepic.jpeg',upload_to='profile_pictures')
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

