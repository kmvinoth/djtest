from django.db import models
from projects.models import Project, User


class ProjectMetadata(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    dummy_pmd_field1 = models.CharField(max_length=20)
    dummy_pmd_field2 = models.CharField(max_length=20)

    def __str__(self):
        return self.project.project_name

    class Meta:
        verbose_name_plural = 'ProjectMetadata'


class DataDepositMetadata(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    dummy_ddmd_field1 = models.CharField(max_length=20)
    dummy_ddmd_field2 = models.CharField(max_length=20)

    def __str__(self):
        return self.data_deposit.deposit_name

    class Meta:
        verbose_name_plural = 'DataDepositMetadata'


class DataObjectMetadata(models.Model):
    data_deposit = models.ForeignKey(DataDepositMetadata, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    dummy_domd_field1 = models.CharField(max_length=20)
    dummy_domd_field2 = models.CharField(max_length=20)

    def __str__(self):
        return self.data_object.object_name

    class Meta:
        verbose_name_plural = 'DataObjectMetadata'


class CompleteMetadata(models.Model):
    project_md = models.ForeignKey(ProjectMetadata)
    data_object_md = models.ForeignKey(DataObjectMetadata)
    data_deposit_md = models.ForeignKey(DataDepositMetadata)

    def __str__(self):
        return self.project_md.project.project_name

    class Meta:
        verbose_name_plural = 'CompleteMetadata'
