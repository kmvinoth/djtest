from django.db import models
from projects.models import Project, User


class MetaDataAttributes(models.Model):
    key = models.CharField(default='key', max_length=50)
    label = models.CharField(default='label', max_length=50)
    value = models.CharField(default='value', max_length=50)
    type = models.CharField(default='type', max_length=50)

    def __str__(self):
        return self.label

    class Meta:
        verbose_name_plural = 'MetaDataAttributes'


class ProjectMetadata(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    form_fields = models.ForeignKey(MetaDataAttributes, blank=True, null=True)

    def __str__(self):
        return self.project.project_name

    class Meta:
        verbose_name_plural = 'ProjectMetadata'
