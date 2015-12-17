# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gics', '0010_auto_20151217_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='is_speaker',
        ),
        migrations.AlterField(
            model_name='person',
            name='favorite_schools',
            field=models.ManyToManyField(blank=True, related_name='favorited', null=True, to='gics.School'),
        ),
    ]
