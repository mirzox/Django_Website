from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, is_password_usable
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def set_password(sender, instance, *args, **kwargs):
    password = make_password(instance.password)
    User.objects.filter(pk=instance.id).update(password=password)

