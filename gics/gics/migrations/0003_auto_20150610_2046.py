# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gics', '0002_auto_20150610_1923'),
    ]

    operations = [
        migrations.AddField(
            model_name='discipline',
            name='slug',
            field=models.SlugField(max_length=64, default='discipline'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='statement',
            field=models.CharField(max_length=512),
        ),
    ]
