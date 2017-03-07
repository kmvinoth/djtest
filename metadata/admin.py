from django.contrib import admin
from .models import ProjectMetadata, MetaDataAttributes


class ProjectMetadataAdmin(admin.ModelAdmin):
    list_display = ['project', 'form_fields']


class MetaDataAttributesAdmin(admin.ModelAdmin):
    list_display = ['key', 'label', 'value', 'type']


admin.site.register(ProjectMetadata, ProjectMetadataAdmin)
admin.site.register(MetaDataAttributes, MetaDataAttributesAdmin)



