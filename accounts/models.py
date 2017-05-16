"""
This module contains the models necessary for the accounts app

"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    """
    A Profile Model for creating and updating User profile

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(blank=True, null=True)
    nickname = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'UserProfile'


class MyUsers(models.Model):
    """
    Extended(django user) User Model for creating local user's by the project admin.

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name="created_by", null=True)

    def __str__(self):
        return self.created_by

    class Meta:
        verbose_name_plural = "MyUsers"

"""  Signal functions, these will be later moved to signal.py inside accounts app """


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Whenever a User Model is created a User profile is created.

    ref : https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html

    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """

    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Whenever a User Model is saved a User profile is saved.
    :param sender:
    :param instance:
    :param kwargs:
    :return:
    """
    instance.userprofile.save()
