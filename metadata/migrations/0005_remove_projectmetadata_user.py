# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0004_auto_20170307_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmetadata',
            name='user',
        ),
    ]
