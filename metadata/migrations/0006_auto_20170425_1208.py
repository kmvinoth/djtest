# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0005_auto_20170425_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metadataattributes',
            name='meta_data_level',
            field=models.IntegerField(choices=[(1, 'Project_md'), (2, 'Deposit_md'), (3, 'Object_md')], default='PROJECT_MD'),
        ),
        migrations.AlterField(
            model_name='metadataattributes',
            name='meta_data_type',
            field=models.IntegerField(choices=[(1, 'Mandatory'), (2, 'Custom')], default='MANDATORY'),
        ),
        migrations.AlterField(
            model_name='metadataattributes',
            name='type',
            field=models.IntegerField(choices=[(1, 'Text'), (2, 'Integer')], default='TEXT'),
        ),
    ]
