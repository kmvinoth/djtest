from django.contrib import admin
from .models import ProjectMetadata, DataObjectMetadata, DataDepositMetadata, CompleteMetadata


class ProjectMetadataAdmin(admin.ModelAdmin):
    list_display = ['project', 'dummy_pmd_field1', 'dummy_pmd_field2']


class DataObjectMetadataAdmin(admin.ModelAdmin):
    list_display = ['data_object', 'dummy_domd_field1', 'dummy_domd_field2']


class DataDepositMetadataAdmin(admin.ModelAdmin):
    list_display = ['data_deposit', 'dummy_ddmd_field1', 'dummy_ddmd_field2']


class CompleteMetadataAdmin(admin.ModelAdmin):
    list_display = ['project_md', 'data_object_md', 'data_deposit_md']

admin.site.register(ProjectMetadata, ProjectMetadataAdmin)
admin.site.register(DataObjectMetadata, DataObjectMetadataAdmin)
admin.site.register(DataDepositMetadata, DataDepositMetadataAdmin)
admin.site.register(CompleteMetadata, CompleteMetadataAdmin)


