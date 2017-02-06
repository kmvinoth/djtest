from django.db import models
from projects.models import Project, DataObject, DataDeposit
# Create your models here.


class ProjectMetadata(models.Model):
    project = models.ForeignKey(Project)
    dummy_pmd_field1 = models.CharField(max_length=20)
    dummy_pmd_field2 = models.CharField(max_length=20)

    def __str__(self):
        return self.project.project_name

    class Meta:
        verbose_name_plural = 'ProjectMetadata'


class DataObjectMetadata(models.Model):
    data_object = models.ForeignKey(DataObject)
    dummy_domd_field1 = models.CharField(max_length=20)
    dummy_domd_field2 = models.CharField(max_length=20)

    def __str__(self):
        return self.data_object.object_name

    class Meta:
        verbose_name_plural = 'DataObjectMetadata'


class DataDepositMetadata(models.Model):
    data_deposit = models.ForeignKey(DataDeposit)
    dummy_ddmd_field1 = models.CharField(max_length=20)
    dummy_ddmd_field2 = models.CharField(max_length=20)

    def __str__(self):
        return self.data_deposit.deposit_name

    class Meta:
        verbose_name_plural = 'DataDepositMetadata'


class CompleteMetadata(models.Model):
    project_md = models.ForeignKey(ProjectMetadata)
    data_object_md = models.ForeignKey(DataObjectMetadata)
    data_deposit_md = models.ForeignKey(DataDepositMetadata)

    def __str__(self):
        return self.project_md.project.project_name

    class Meta:
        verbose_name_plural = 'CompleteMetadata'
