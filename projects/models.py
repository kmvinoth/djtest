from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver


class Project(models.Model):
    project_name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, blank=True, null=True)
    info = models.TextField(max_length=500, default='Add some info about your project')

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name_plural = 'Project'


class Deposit(models.Model):
    project = models.ForeignKey(Project)
    deposit_name = models.CharField(default='some_name', max_length=20)
    user = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.deposit_name

    class Meta:
        verbose_name_plural = 'Deposit'


class DataObject(models.Model):
    deposit = models.ForeignKey(Deposit)
    data_object_name = models.CharField(default='some_name', max_length=20)
    user = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.data_object_name

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


@receiver(post_save, sender=Deposit)
def create_data_object(sender, instance, created, **kwargs):
    """
    Signal for creating data object once a deposit has been created
    """

    if created:
        DataObject.objects.create(deposit=instance)

    else:
        print('deposit metadata attribute not created')


