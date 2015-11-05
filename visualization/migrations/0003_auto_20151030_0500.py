# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0002_auto_20151030_0455'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search_data',
            name='chart_type',
        ),
        migrations.RemoveField(
            model_name='search_data',
            name='subtitle_text',
        ),
        migrations.RemoveField(
            model_name='search_data',
            name='title_text',
        ),
        migrations.RemoveField(
            model_name='search_data',
            name='yaxis_title_text',
        ),
    ]
