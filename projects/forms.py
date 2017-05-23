"""
This Module contains the Model Forms for the projects app.

ProjectInfoForm = Used to add and edit info the project,
ProjectMemberRoleForm = Used to assign & edit role to the project member,
DepositForm = Used for entering meta data related to Deposit session,
DataObjectForm = Used for entering metadata related to DataObject

"""

from django import forms
from .models import Project, ProjectMemberRole, Deposit, DataObject


class ProjectInfoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProjectInfoForm, self).__init__(*args, **kwargs)
        # Read only field, so that project admin cannot edit
        # Not foolproof because you can edit the Html and alter the value, during Post
        # Ref : http://techstream.org/Bits/Read-only-field-in-django-ModelForm
        self.fields['project_name'].widget.attrs['readonly'] = True

    class Meta:
        model = Project
        fields = ['project_name', 'admin', 'info']


class ProjectMemberRoleForm(forms.ModelForm):
    # Make the Project field and the Member field Read only to the project admin,
    # he can only edit the role of the memeber in the project
    # Hint do it by altering the form __init__ method
    class Meta:
        model = ProjectMemberRole
        fields = ['project', 'member', 'role']


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'


class DataobjectForm(forms.ModelForm):
    class Meta:
        model = DataObject
        fields = ['data_object_name']
