from django.dispatch import receiver
from .models import Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_user(instance, created, sender, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def create_user(instance, sender, **kwargs):
    instance.profile.save()


