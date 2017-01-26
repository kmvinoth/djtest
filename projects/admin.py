from django.contrib import admin
from .models import Project, ProjectUserRole


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'admin']


class ProjectUserRoleAdmin(admin.ModelAdmin):
    list_display = ['project', 'user', 'role']

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectUserRole, ProjectUserRoleAdmin)


