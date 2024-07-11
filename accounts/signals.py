from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from .models import User,UserProfile


@receiver(post_save,sender=User)
def post_save_create_profile_reciver(sender,instance,created,**kwargs):
    print(created)
    # for newly creating user profile automatically
    if created:
        UserProfile.objects.create(user=instance)
    else:
        # for updating the existing userprofile
        try:
            profile=UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create the userprofile if not exist
            UserProfile.objects.create(user=instance)

@receiver(post_save,sender=User)
def pre_save_profile_receiver(sender,instance,**kwrgs):
    pass