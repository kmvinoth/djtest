from django.contrib import admin
from .models import ProjectMetadata


class ProjectMetadataAdmin(admin.ModelAdmin):
    list_display = ['project', 'dummy_pmd_field1', 'dummy_pmd_field2']


admin.site.register(ProjectMetadata, ProjectMetadataAdmin)



