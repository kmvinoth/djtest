from django.contrib import admin
from .models import Project, ProjectMemberRole


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'admin']


class ProjectMemberRoleAdmin(admin.ModelAdmin):
    list_display = ['project', 'member', 'role']


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMemberRole, ProjectMemberRoleAdmin)


