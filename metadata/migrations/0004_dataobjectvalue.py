# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_dataobject_user'),
        ('metadata', '0003_depositvalue'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataobjectValue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('val', models.CharField(blank=True, max_length=50)),
                ('dataobject', models.ForeignKey(to='projects.DataObject')),
                ('md_attributes', models.ForeignKey(to='metadata.MetadataAttributes')),
            ],
            options={
                'verbose_name_plural': 'DataobjectValue',
            },
        ),
    ]
