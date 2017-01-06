from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=100, default=True, blank=True)

    class Meta:
        verbose_name_plural = 'Project'
