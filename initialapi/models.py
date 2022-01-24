from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.db.models.signals import post_save
from django.dispatch import receiver


class OneTimeCode(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.IntegerField()
    attempt = models.IntegerField(default=0)
    is_blocked = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'AttemptResetPassword'
        verbose_name_plural = 'AttemptsResetPassword'

    def __str__(self):
        return f'{self.user_id} - {self.attempt} - {self.is_blocked}'


@receiver(post_save, sender=User)
def set_password(sender, instance, created, **kwargs):
    if "pbkdf2_sha256" not in instance.password and created:
        password = make_password(instance.password)
        User.objects.filter(pk=instance.id).update(password=password)


@receiver(post_save, sender=OneTimeCode)
def check_status(sender, instance, *args, **kwargs):
    if instance.attempt == 5:
        OneTimeCode.objects.filter(pk=instance.id).update(is_blocked=True)
