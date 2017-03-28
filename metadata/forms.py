from django import forms
from .models import Value, Project
from django.forms import inlineformset_factory

value_inline_form_set = inlineformset_factory(Project,  Value, fields=('md_attributes', 'val',),
                                                  max_num=0, can_delete=False, extra=0)


class MetadataForm(forms.ModelForm):
    class Meta:
        model = Value
        fields = ['project']

    def __init__(self, *args, **kwargs):
        super(MetadataForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.filter(project_name='OPUS')
