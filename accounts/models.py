from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'UserProfile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Projects(models.Model):
    project_name = models.CharField(max_length=100, default=True, blank=True)

    class Meta:
        verbose_name_plural = 'Projects'


class Home(models.Model):
    home_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Home'

    def __str__(self):
        self.home_name

