from django.contrib import admin
from .models import Project, ProjectMemberRole, Deposit, DepositSessionStatus, DataObject


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'admin']


class DepositAdmin(admin.ModelAdmin):
    list_display = ['project', 'deposit_name']


class DepositSessionStatusAdmin(admin.ModelAdmin):
    list_display = ['deposit_name', 'status']


class DataobjectAdmin(admin.ModelAdmin):
    list_display = ['deposit', 'data_object_name']


class ProjectMemberRoleAdmin(admin.ModelAdmin):
    list_display = ['project', 'member', 'role']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(DepositSessionStatus, DepositSessionStatusAdmin)
admin.site.register(DataObject, DataobjectAdmin)
admin.site.register(ProjectMemberRole, ProjectMemberRoleAdmin)


