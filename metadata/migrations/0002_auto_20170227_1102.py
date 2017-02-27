# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('metadata', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmetadata',
            name='project',
            field=models.ForeignKey(to='projects.Project', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='projectmetadata',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dataobjectmetadata',
            name='data_deposit',
            field=models.ForeignKey(to='metadata.DataDepositMetadata', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='dataobjectmetadata',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='datadepositmetadata',
            name='project',
            field=models.ForeignKey(to='projects.Project', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='datadepositmetadata',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True),
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
