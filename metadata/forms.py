"""
This Module contains the Model Forms for the metadata app.

MetadataAttributesForm = Form for entering new metadata fields.

value_inline_form_set = Form for entering project metadata values.
deposit_value_inline_form_set = Form for entering deposit metadata values.
data_object_value_inline_form_set = Form for entering data object metadata values.

For more information on how inline formset works see django documentation under

https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/#using-an-inline-formset-in-a-view

"""

from django import forms
from .models import Value, Project, MetadataAttributes, Deposit, DepositValue, DataObject, DataObjectValue
from django.forms import inlineformset_factory

value_inline_form_set = inlineformset_factory(Project,  Value, fields=('md_attributes', 'val',),
                                              max_num=0, can_delete=False, extra=0)

deposit_value_inline_form_set = inlineformset_factory(Deposit, DepositValue, fields=('md_attributes', 'val',),
                                                      max_num=0, can_delete=False, extra=0)

data_object_value_inline_form_set = inlineformset_factory(DataObject, DataObjectValue, fields=('md_attributes', 'val',),
                                                          max_num=0, can_delete=False, extra=0)


class MetadataAttributesForm(forms.ModelForm):
    class Meta:
        model = MetadataAttributes
        fields = '__all__'
