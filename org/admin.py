from django.contrib import admin
from django.contrib.auth.models import User
from .models import Projects, ProjectUser


class ProjectsAdmin(admin.ModelAdmin):
    list_display = 'projectName',


class ProjectUserAdmin(admin.ModelAdmin):
    list_display = 'project_name', 'user', 'created_by'

    # def get_queryset(self, request):
    #     qs = super(ProjectUserAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(created_by=request.user)


admin.site.register(Projects, ProjectsAdmin)
admin.site.register(ProjectUser, ProjectUserAdmin)