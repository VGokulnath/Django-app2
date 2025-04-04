from django.db.models.signals import post_save   # whenever the user model is saved we will get a signal
from django.contrib.auth.models import User
from django.dispatch import receiver   # receives a signal in our case it is create a profile
from .models import Profile


@receiver(post_save,sender=User)
def build_profile(sender,instance,created,**kwargs):#sender - sends signals, instance - user from form.save , created - boolean value wheather user is created or not? , 
    if created:
        Profile.objects.create(user = instance)

        
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()


