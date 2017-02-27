from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, blank=True, null=True)
    info = models.TextField(max_length=500, default='Add some info about your project')

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name_plural = 'Project'


class ProjectMemberRole(models.Model):
    project = models.ForeignKey(Project)
    member = models.ForeignKey(User)
    role = models.ForeignKey(Group)

    def __str__(self):
        return self.project.project_name

    class Meta:
        verbose_name_plural = 'ProjectMemberRole'


