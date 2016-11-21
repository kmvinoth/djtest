from django.db import models
from django.contrib.auth.models import User


class Projects(models.Model):
    projectName = models.CharField(max_length=50, default="project1")

    class Meta:
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.projectName


class ProjectUser(models.Model):
    project_name = models.ForeignKey(Projects)
    user = models.OneToOneField(User)
    created_by = models.ForeignKey(User, related_name='projectadmin')

    class Meta:
        verbose_name_plural = 'ProjectUser'