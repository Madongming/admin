# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualization', '0003_auto_20151030_0500'),
    ]

    operations = [
        migrations.AddField(
            model_name='search_data',
            name='pic_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
