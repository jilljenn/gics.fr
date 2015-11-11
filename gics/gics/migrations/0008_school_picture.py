# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gics', '0007_auto_20151105_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='picture',
            field=models.ForeignKey(to='gics.Document', null=True, blank=True),
        ),
    ]
