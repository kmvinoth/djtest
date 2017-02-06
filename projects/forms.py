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


class ProjectMemberRoleEditForm(forms.ModelForm):

    # Make the Project field and the Member field Read only to the project admin,
    # he can only edit the role of the memeber in the project
    # Hint do it by altering the form __init__ method
    class Meta:
        model = ProjectMemberRole
        fields = ['project', 'member', 'role']
