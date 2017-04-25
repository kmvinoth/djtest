from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from projects.models import Project, Deposit, DataObject, User

from .fields import KeySlugField


class MetadataAttributes(models.Model):

    DATA_TYPE_CHOICES = (('text', 'Text'), ('int', 'Integer'))
    MD_TYPE_CHOICES = (('mandatory', 'Mandatory'), ('custom', 'Custom'))
    MD_LEVEL_CHOICES = (('project_md', 'Project_MD'), ('deposit_md', 'Deposit_MD'), ('object_md', 'Object_MD'),)

    label = models.CharField(max_length=50)
    key = KeySlugField(max_length=50, db_index=True, blank=True)
    type = models.CharField(max_length=10, choices=DATA_TYPE_CHOICES, default='text')
    # Remember to do type validation later
    meta_data_type = models.CharField(max_length=10, choices=MD_TYPE_CHOICES, default='mandatory')
    meta_data_level = models.CharField(max_length=10, choices=MD_LEVEL_CHOICES, default='project_md')

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
    project = models.ForeignKey(Project)
    md_attributes = models.ForeignKey(MetadataAttributes)
    val = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.val

    class Meta:
        verbose_name_plural = 'Value'


class DepositValue(models.Model):
    deposit = models.ForeignKey(Deposit)
    md_attributes = models.ForeignKey(MetadataAttributes)
    val = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.val

    class Meta:
        verbose_name_plural = 'DepositValue'


class DataObjectValue(models.Model):
    dataobject = models.ForeignKey(DataObject)
    md_attributes = models.ForeignKey(MetadataAttributes)
    val = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.val

    class Meta:
        verbose_name_plural = 'DataobjectValue'


@receiver(post_save, sender=Project)
def create_entry_in_value(sender, instance, created, **kwargs):
    """
    Whenever a project is created, the value table gets populated with all the static metadata attributes
    """

    if created:
        attributes = MetadataAttributes.objects.filter(meta_data_level='project_md', meta_data_type='mandatory')
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
        attributes = MetadataAttributes.objects.filter(meta_data_level='deposit_md')
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
        attributes = MetadataAttributes.objects.filter(meta_data_level='object_md')
        for attr in attributes:
            DataObjectValue.objects.create(dataobject=instance, md_attributes=attr)
    else:
        print('dataobject metadata attribute not created')

