from django.db import models
from projects.models import Project, User


class ProjectMetadata(models.Model):
    project = models.ForeignKey(Project, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    key = models.CharField(default='key', max_length=50)
    label = models.CharField(default='label', max_length=50)
    value = models.CharField(default='value', max_length=50)
    type = models.CharField(default='type', max_length=50)

    def __str__(self):
        return self.project.project_name

    class Meta:
        verbose_name_plural = 'ProjectMetadata'
