from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    admin = models.ForeignKey(User)

    class Meta:
        verbose_name_plural = 'Project'
