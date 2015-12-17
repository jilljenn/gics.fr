# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gics', '0011_auto_20151217_0118'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userhistory',
            options={'verbose_name_plural': 'user histories', 'ordering': ['-date']},
        ),
    ]
