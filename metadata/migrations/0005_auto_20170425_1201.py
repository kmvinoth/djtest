# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0004_dataobjectvalue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadataattributes',
            name='meta_data_level',
            field=models.IntegerField(default='PROJECT_MD', choices=[('PROJECT_MD', 'Project_md'), ('DEPOSIT_MD', 'Deposit_md'), ('OBJECT_MD', 'Object_md')]),
        ),
        migrations.AlterField(
            model_name='metadataattributes',
            name='meta_data_type',
            field=models.IntegerField(default='MANDATORY', choices=[('MANDATORY', 'Mandatory'), ('CUSTOMARY', 'Custom')]),
        ),
        migrations.AlterField(
            model_name='metadataattributes',
            name='type',
            field=models.IntegerField(default='Text', choices=[('TEXT', 'Text'), ('INT', 'Integer')]),
        ),
    ]
