# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('home_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Home',
            },
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'UserProfile'},
        ),
    ]
