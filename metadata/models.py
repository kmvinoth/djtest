"""
This module contains the models necessary for the metadata app

"""

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from projects.models import Project, Deposit, DataObject, User

from .fields import KeySlugField


class MetadataAttributes(models.Model):
    """
    A Model for the metadata fields

    """

    TEXT = 'Text'
    INT = 'Integer'
    DATA_TYPE_CHOICES = ((TEXT, 'Text'), (INT, 'Integer'))

    MANDATORY = 'Mandatory'
    CUSTOMARY = 'Customary'
    MD_TYPE_CHOICES = ((MANDATORY, 'Mandatory'), (CUSTOMARY, 'Custom'))

    PROJECT_MD = 'Project Metadata'
    DEPOSIT_MD = 'Deposit Metadata'
    OBJECT_MD = 'DataObject Metadata'
    MD_LEVEL_CHOICES = ((PROJECT_MD, 'Project_md'), (DEPOSIT_MD, 'Deposit_md'), (OBJECT_MD, 'Object_md'),)
    # ref(encapsulation) : http://www.b-list.org/weblog/2007/nov/02/handle-choices-right-way/

    label = models.CharField(max_length=50)
    key = KeySlugField(max_length=50, db_index=True, blank=True)
    type = models.CharField(choices=DATA_TYPE_CHOICES, default=TEXT, max_length=25)
    # Remember to do type validation later
    meta_data_type = models.CharField(choices=MD_TYPE_CHOICES, default=MANDATORY, max_length=25)
    meta_data_level = models.CharField(choices=MD_LEVEL_CHOICES, default=PROJECT_MD, max_length=25)

    class Meta:
        verbose_name_plural = 'MetaDataAttributes'

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        """
        Saves the Attribute and auto-generates a key(slug) field if one wasn't
        provided.
        """
        if not self.key:
            self.key = KeySlugField.create_slug_from_name(self.label)
        self.full_clean()
        super(MetadataAttributes, self).save(*args, **kwargs)


class Value(models.Model):
    """
    A Model for storing the  fields associated with Project Metadata Value only
    For more information see the Pdf associated with the documentation

    """

    project = models.ForeignKey(Project)
    md_attributes = models.ForeignKey(MetadataAttributes)
    val = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.val

    class Meta:
        verbose_name_plural = 'Value'


class DepositValue(models.Model):
    """
    A Model for storing the  fields associated with Deposit Metadata Value only

    """
    deposit = models.ForeignKey(Deposit)
    md_attributes = models.ForeignKey(MetadataAttributes)
    val = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.val

    class Meta:
        verbose_name_plural = 'DepositValue'


class DataObjectValue(models.Model):
    """
    A Model for storing the  fields associated with Dataobject Metadata Value only

    """
    dataobject = models.ForeignKey(DataObject)
    md_attributes = models.ForeignKey(MetadataAttributes)
    val = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.val

    class Meta:
        verbose_name_plural = 'DataobjectValue'


"""  Signal functions, these will be later moved to signal.py inside metadata app """


@receiver(post_save, sender=Project)
def create_entry_in_value(sender, instance, created, **kwargs):
    """
    Whenever a project is created, the value table gets populated with all the static metadata attributes
    You can customize this by filtering the MetadataAttributes Table
    """

    if created:
        attributes = MetadataAttributes.objects.filter(meta_data_level=MetadataAttributes.PROJECT_MD,
                                                       meta_data_type=MetadataAttributes.MANDATORY)
        for attr in attributes:
            Value.objects.create(project=instance, md_attributes=attr)
    else:
        print('project metadata attribute not created')


@receiver(post_save, sender=Deposit)
def create_entry_in_deposit_value(sender, instance, created, **kwargs):
    """
    Whenever a Deposit is created, the deposit_value table gets populated with all the static deposit
    metadata attributes
    """

    if created:
        attributes = MetadataAttributes.objects.filter(meta_data_level=MetadataAttributes.DEPOSIT_MD)
        for attr in attributes:
            DepositValue.objects.create(deposit=instance, md_attributes=attr)
    else:
        print('deposit metadata attribute not created')


@receiver(post_save, sender=DataObject)
def create_entry_in_dataobject_value(sender, instance, created, **kwargs):
    """
    Whenever a DataObject is created, the dataobject_value table gets populated with all the static deposit
    metadata attributes
    """

    if created:
        attributes = MetadataAttributes.objects.filter(meta_data_level=MetadataAttributes.OBJECT_MD)
        for attr in attributes:
            DataObjectValue.objects.create(dataobject=instance, md_attributes=attr)
    else:
        print('dataobject metadata attribute not created')

