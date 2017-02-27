from django import forms
from .models import ProjectMetadata, DataDepositMetadata


class ProjectMetadataForm(forms.ModelForm):
    class Meta:
        model = ProjectMetadata
        fields = ['project', 'user', 'dummy_pmd_field1', 'dummy_pmd_field2']


class DepositMetadataForm(forms.ModelForm):
    class Meta:
        model = DataDepositMetadata
        fields = ['project', 'user', 'dummy_ddmd_field1', 'dummy_ddmd_field2']
