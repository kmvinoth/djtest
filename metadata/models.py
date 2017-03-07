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