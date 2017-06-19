"""

This module contains the models necessary for the projects app

"""
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


class Project(models.Model):
    """

    A Project Model for creating a Project with name, admin and some info

    """
    project_name = models.CharField(max_length=100)
    admin = models.ForeignKey(User, blank=True, null=True)
    info = models.TextField(max_length=500, default='Add some info about your project')

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name_plural = 'Project'


class Deposit(models.Model):
    """

    A Deposit Model for creating a Deposit Session

    """
    project = models.ForeignKey(Project)
    deposit_name = models.SlugField(max_length=50, db_index=True, blank=True, unique=True)
    user = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.deposit_name

    # ref : http://fazle.me/auto-generating-unique-slug-in-django/
    def _get_unique_deposit_name(self):
        """

        Create a unique deposit name by taking the project name and the username

        """
        deposit_string = self.project.project_name + '_' + self.user.username + '_' + 'deposit'
        deposit_name = slugify(deposit_string)
        unique_slug = deposit_name
        num = 1
        while Deposit.objects.filter(deposit_name=unique_slug).exists():
            unique_slug = '{}_{}'.format(deposit_name, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.deposit_name:
            self.deposit_name = self._get_unique_deposit_name()
        super().save()

    class Meta:
        verbose_name_plural = 'Deposit'


class DepositSessionStatus(models.Model):
    """

        A DepositSessionStatus model for displaying the status of the Deposit session.

        Should have added another field (Status) to the deposit model.Since the DepositSession is purged from
        the database once the user closes the session, it is necessary to have
        a separate table to know the status of the deposit session.

    """
    OPEN = 1
    CLOSED = 0
    STATUS_CHOICES = ((OPEN, 'Open'), (CLOSED, 'Closed'))

    deposit_name = models.CharField(max_length=100, default="SampleName")
    status = models.IntegerField(choices=STATUS_CHOICES, default=OPEN)
    user = models.ForeignKey(User, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'DepositSessionStatus'


class DataObject(models.Model):
    """

    A DataObject model for creating a dataobject inside a Deposit Session

    """
    deposit = models.ForeignKey(Deposit)
    data_object_name = models.SlugField(max_length=50, db_index=True, blank=True, unique=True)
    user = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.data_object_name

    # ref : http://fazle.me/auto-generating-unique-slug-in-django/
    def _get_unique_data_object_name(self):
        """
        Create a unique data object name by taking the deposit name
        """
        data_object_string = self.deposit.deposit_name + '_' + 'object'
        data_object_name = slugify(data_object_string)
        unique_slug = data_object_name
        num = 1
        # Since unique slug already exists(i.e deposit-number) the while loop is not executed and it will always return
        # deposit_name + object (Add further logic depends on the situation)
        while DataObject.objects.filter(data_object_name=unique_slug).exists():
            unique_slug = '{}_{}'.format(data_object_name, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.data_object_name:
            self.data_object_name = self._get_unique_data_object_name()
        super().save()

    class Meta:
        verbose_name_plural = 'DataObject'


class ProjectMemberRole(models.Model):
    """

    Model for assigning role to a member of the project

    """
    project = models.ForeignKey(Project)
    member = models.ForeignKey(User)
    role = models.ForeignKey(Group)

    def __str__(self):
        return self.project.project_name

    class Meta:
        verbose_name_plural = 'ProjectMemberRole'


"""  Signal functions, these will be later moved to signal.py inside projects app """


@receiver(post_save, sender=Deposit)
def create_data_object(sender, instance, created, **kwargs):
    """

    Signal for creating dataobject once a deposit session has been created

    """

    if created:
        DataObject.objects.create(deposit=instance)

    else:
        print('deposit metadata attribute not created')


@receiver(post_save, sender=Deposit)
def create_deposit_status(sender, instance, created, **kwargs):
    """

    Signal for creating Deposit Session status once a deposit session has been created

    """

    if created:
        DepositSessionStatus.objects.create(deposit_name=instance.deposit_name)

    else:
        print('deposit session status not created')


