# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gics', '0012_auto_20151217_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='favorite_schools',
            field=models.ManyToManyField(to='gics.School', related_name='favorited', blank=True),
        ),
    ]
