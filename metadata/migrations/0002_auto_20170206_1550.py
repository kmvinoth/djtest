# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datadepositmetadata',
            name='data_deposit',
            field=models.ForeignKey(to='projects.DataDeposit'),
        ),
    ]
