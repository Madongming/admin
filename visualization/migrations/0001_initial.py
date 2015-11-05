# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monitor_name', models.CharField(max_length=50)),
                ('index', models.CharField(max_length=50)),
                ('query', models.CharField(max_length=50, null=True)),
                ('fields', models.CharField(max_length=500, null=True)),
                ('field', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('size', models.IntegerField(null=True)),
                ('sub_fields', models.CharField(max_length=500, null=True)),
                ('mothod_type', models.CharField(max_length=20)),
            ],
        ),
    ]
