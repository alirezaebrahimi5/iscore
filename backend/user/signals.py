from django.db.models.signals import post_save, post_delete

from .models import User, Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        user=instance
        if user.is_active and user.is_staff and user.is_superuser:
            role = 1
        else:
            role = 7

        new_profile = Profile.objects.create(
            user=user,
            role = role
        )
        

def delete_user(sender, instance, **kwargs):
    user = instance.user
    user.delete()


post_save.connect(create_profile, sender=User)


post_delete.connect(delete_user, sender=Profile)
