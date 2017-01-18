from django import forms
from .models import Project


class ProjectInfoForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'admin', 'info']

