# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteMetadata',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
            options={
                'verbose_name_plural': 'CompleteMetadata',
            },
        ),
        migrations.CreateModel(
            name='DataDepositMetadata',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('dummy_ddmd_field1', models.CharField(max_length=20)),
                ('dummy_ddmd_field2', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'DataDepositMetadata',
            },
        ),
        migrations.CreateModel(
            name='DataObjectMetadata',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('dummy_domd_field1', models.CharField(max_length=20)),
                ('dummy_domd_field2', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'DataObjectMetadata',
            },
        ),
        migrations.CreateModel(
            name='ProjectMetadata',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('dummy_pmd_field1', models.CharField(max_length=20)),
                ('dummy_pmd_field2', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'ProjectMetadata',
            },
        ),
    ]
