from django import forms
from .models import Project, ProjectMemberRole


class ProjectInfoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # Figure out how super works...!
        super(ProjectInfoForm, self).__init__(*args, **kwargs)
        # Read only field, so that project admin cannot edit
        # Not foolproof because you can edit the Html and alter the value, during Post
        # Ref : http://techstream.org/Bits/Read-only-field-in-django-ModelForm
        self.fields['project_name'].widget.attrs['readonly'] = True

    class Meta:
        model = Project
        fields = ['project_name', 'admin', 'info']


class ProjectMemberRoleForm(forms.ModelForm):
    class Meta:
        model = ProjectMemberRole
        fields = ['project', 'member', 'role']
