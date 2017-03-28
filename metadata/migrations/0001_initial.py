# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import metadata.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetadataAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('key', metadata.fields.KeySlugField(blank=True)),
                ('type', models.CharField(default='text', max_length=10, choices=[('text', 'Text'), ('int', 'Integer')])),
                ('meta_data_type', models.CharField(default='mandatory', max_length=10, choices=[('mandatory', 'Mandatory'), ('custom', 'Custom')])),
                ('meta_data_level', models.CharField(default='project_md', max_length=10, choices=[('project_md', 'Project_MD'), ('deposit_md', 'Deposit_MD'), ('object_md', 'Object_MD')])),
            ],
            options={
                'verbose_name_plural': 'MetaDataAttributes',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val', models.CharField(max_length=50, blank=True)),
                ('md_attributes', models.ForeignKey(to='metadata.MetadataAttributes')),
            ],
            options={
                'verbose_name_plural': 'Value',
            },
        ),
    ]
