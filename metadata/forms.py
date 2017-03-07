from django import forms
from .models import ProjectMetadata


class ProjectMetadataForm(forms.ModelForm):
    class Meta:
        model = ProjectMetadata
        fields = ['project', 'user', 'label']
