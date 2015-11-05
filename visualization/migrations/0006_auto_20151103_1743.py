# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0005_search_data_id_in_dashboard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search_data',
            name='id_in_dashboard',
        ),
        migrations.AddField(
            model_name='search_data',
            name='num_dashboard',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
