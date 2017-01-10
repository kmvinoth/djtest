from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    fields = ['project_name', 'admin']

admin.site.register(Project, ProjectAdmin)

