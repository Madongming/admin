# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0004_search_data_pic_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_data',
            name='id_in_dashboard',
            field=models.BooleanField(default=False),
        ),
    ]
