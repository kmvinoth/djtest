# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
        ('metadata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
        ),
    ]
