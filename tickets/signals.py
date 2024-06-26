from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.apps import apps

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    Profile = apps.get_model('tickets', 'Profile')
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()