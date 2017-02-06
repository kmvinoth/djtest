from django import forms
from .models import ProjectMetadata


class ProjectMetadataForm(forms.ModelForm):
    class Meta:
        model = ProjectMetadata
        fields = ['project', 'dummy_pmd_field1', 'dummy_pmd_field2']
