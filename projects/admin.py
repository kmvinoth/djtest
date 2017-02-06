from django.contrib import admin
from .models import Project, ProjectMemberRole, DataObject, DataDeposit


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'admin']


class ProjectMemberRoleAdmin(admin.ModelAdmin):
    list_display = ['project', 'member', 'role']


class DataObjectAdmin(admin.ModelAdmin):
    list_display = ['project', 'object_name']


class DataDepositAdmin(admin.ModelAdmin):
    list_display = ['object_name', 'deposit_name']

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMemberRole, ProjectMemberRoleAdmin)
admin.site.register(DataObject, DataObjectAdmin)
admin.site.register(DataDeposit, DataDepositAdmin)


