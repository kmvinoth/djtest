from django import forms
from .models import Project, ProjectMemberRole


class ProjectInfoForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'admin', 'info']


class ProjectMemberRoleForm(forms.ModelForm):
    class Meta:
        model = ProjectMemberRole
        fields = ['project', 'member', 'role']
