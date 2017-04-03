# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20170403_1013'),
        ('metadata', '0002_value_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositValue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('val', models.CharField(max_length=50, blank=True)),
                ('deposit', models.ForeignKey(to='projects.Deposit')),
                ('md_attributes', models.ForeignKey(to='metadata.MetadataAttributes')),
            ],
            options={
                'verbose_name_plural': 'DepositValue',
            },
        ),
    ]
