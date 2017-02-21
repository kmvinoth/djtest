from django.contrib import admin
from .models import Project, ProjectMemberRole, DataObject, DataDeposit


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'admin']


class ProjectMemberRoleAdmin(admin.ModelAdmin):
    list_display = ['project', 'member', 'role']


class DataDepositAdmin(admin.ModelAdmin):
    list_display = ['project', 'deposit_name']


class DataObjectAdmin(admin.ModelAdmin):
    list_display = ['deposit', 'object_name']


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMemberRole, ProjectMemberRoleAdmin)
admin.site.register(DataObject, DataObjectAdmin)
admin.site.register(DataDeposit, DataDepositAdmin)


