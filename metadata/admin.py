from django.contrib import admin
from .models import ProjectMetadata


class ProjectMetadataAdmin(admin.ModelAdmin):
    list_display = ['project', 'user']


admin.site.register(ProjectMetadata, ProjectMetadataAdmin)



