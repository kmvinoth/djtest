# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0003_auto_20170307_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetaDataAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=50, default='key')),
                ('label', models.CharField(max_length=50, default='label')),
                ('value', models.CharField(max_length=50, default='value')),
                ('type', models.CharField(max_length=50, default='type')),
            ],
            options={
                'verbose_name_plural': 'MetaDataAttributes',
            },
        ),
        migrations.RemoveField(
            model_name='projectmetadata',
            name='key',
        ),
        migrations.RemoveField(
            model_name='projectmetadata',
            name='label',
        ),
        migrations.RemoveField(
            model_name='projectmetadata',
            name='type',
        ),
        migrations.RemoveField(
            model_name='projectmetadata',
            name='value',
        ),
        migrations.AddField(
            model_name='projectmetadata',
            name='form_fields',
            field=models.ForeignKey(blank=True, null=True, to='metadata.MetaDataAttributes'),
        ),
    ]
