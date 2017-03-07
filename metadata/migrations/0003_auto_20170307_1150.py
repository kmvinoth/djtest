# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0002_auto_20170227_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completemetadata',
            name='data_deposit_md',
        ),
        migrations.RemoveField(
            model_name='completemetadata',
            name='data_object_md',
        ),
        migrations.RemoveField(
            model_name='completemetadata',
            name='project_md',
        ),
        migrations.RemoveField(
            model_name='datadepositmetadata',
            name='project',
        ),
        migrations.RemoveField(
            model_name='datadepositmetadata',
            name='user',
        ),
        migrations.RemoveField(
            model_name='dataobjectmetadata',
            name='data_deposit',
        ),
        migrations.RemoveField(
            model_name='dataobjectmetadata',
            name='user',
        ),
        migrations.RemoveField(
            model_name='projectmetadata',
            name='dummy_pmd_field1',
        ),
        migrations.RemoveField(
            model_name='projectmetadata',
            name='dummy_pmd_field2',
        ),
        migrations.AddField(
            model_name='projectmetadata',
            name='key',
            field=models.CharField(max_length=50, default='key'),
        ),
        migrations.AddField(
            model_name='projectmetadata',
            name='label',
            field=models.CharField(max_length=50, default='label'),
        ),
        migrations.AddField(
            model_name='projectmetadata',
            name='type',
            field=models.CharField(max_length=50, default='type'),
        ),
        migrations.AddField(
            model_name='projectmetadata',
            name='value',
            field=models.CharField(max_length=50, default='value'),
        ),
        migrations.DeleteModel(
            name='CompleteMetadata',
        ),
        migrations.DeleteModel(
            name='DataDepositMetadata',
        ),
        migrations.DeleteModel(
            name='DataObjectMetadata',
        ),
    ]
