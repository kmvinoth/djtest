from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    organization = models.CharField(max_length=100, default=True, blank=True)
    phone = models.CharField(max_length=20, default=True, blank=True)


class Projects(models.Model):
   project_name = models.CharField(max_length=100, default=True, blank=True)
