# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20170202_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'CompleteMetadata',
            },
        ),
        migrations.CreateModel(
            name='DataDepositMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummy_ddmd_field1', models.CharField(max_length=20)),
                ('dummy_ddmd_field2', models.CharField(max_length=20)),
                ('data_deposit', models.ForeignKey(to='projects.DataObject')),
            ],
            options={
                'verbose_name_plural': 'DataDepositMetadata',
            },
        ),
        migrations.CreateModel(
            name='DataObjectMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummy_domd_field1', models.CharField(max_length=20)),
                ('dummy_domd_field2', models.CharField(max_length=20)),
                ('data_object', models.ForeignKey(to='projects.DataObject')),
            ],
            options={
                'verbose_name_plural': 'DataObjectMetadata',
            },
        ),
        migrations.CreateModel(
            name='ProjectMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dummy_pmd_field1', models.CharField(max_length=20)),
                ('dummy_pmd_field2', models.CharField(max_length=20)),
                ('project', models.ForeignKey(to='projects.Project')),
            ],
            options={
                'verbose_name_plural': 'ProjectMetadata',
            },
        ),
        migrations.AddField(
            model_name='completemetadata',
            name='data_deposit_md',
            field=models.ForeignKey(to='metadata.DataDepositMetadata'),
        ),
        migrations.AddField(
            model_name='completemetadata',
            name='data_object_md',
            field=models.ForeignKey(to='metadata.DataObjectMetadata'),
        ),
        migrations.AddField(
            model_name='completemetadata',
            name='project_md',
            field=models.ForeignKey(to='metadata.ProjectMetadata'),
        ),
    ]
