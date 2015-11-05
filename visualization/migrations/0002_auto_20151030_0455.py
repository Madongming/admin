# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_data',
            name='chart_type',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='search_data',
            name='subtitle_text',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='search_data',
            name='title_text',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='search_data',
            name='yaxis_title_text',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='search_data',
            name='mothod_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
