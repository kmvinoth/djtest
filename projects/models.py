from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, null=True, blank=True)
    info = models.TextField(max_length=500, default='Hi')

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name_plural = 'Project'


class DataDeposit(models.Model):
    project = models.ForeignKey(Project, null=True, blank=True)
    # naming convention project_object_name
    deposit_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.deposit_name

    class Meta:
        verbose_name_plural = 'DataDeposit'


class DataObject(models.Model):
    deposit = models.ForeignKey(DataDeposit, null=True, blank=True)
    # naming convention project_object_name
    object_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.object_name

    class Meta:
        verbose_name_plural = 'DataObject'


class ProjectMemberRole(models.Model):
    project = models.ForeignKey(Project)
    member = models.ForeignKey(User)
    role = models.ForeignKey(Group)

    def __str__(self):
        return self.project.project_name

    class Meta:
        verbose_name_plural = 'ProjectMemberRole'


