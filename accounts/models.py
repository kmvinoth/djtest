from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    organization = models.CharField(max_length=100, default=True, blank=True)
    phone = models.CharField(max_length=20, default=True, blank=True)

    class Meta:
        verbose_name_plural = 'UserProfile'

    def __str__(self):
        self.user


class Home(models.Model):
    home_name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Home'

    def __str__(self):
        self.home_name