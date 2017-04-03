from django.contrib import admin
from .models import Project, ProjectMemberRole, Deposit


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'admin']


class DepositAdmin(admin.ModelAdmin):
    list_display = ['project', 'deposit_name']


class ProjectMemberRoleAdmin(admin.ModelAdmin):
    list_display = ['project', 'member', 'role']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Deposit, DepositAdmin)
admin.site.register(ProjectMemberRole, ProjectMemberRoleAdmin)


