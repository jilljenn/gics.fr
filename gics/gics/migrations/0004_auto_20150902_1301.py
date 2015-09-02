# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gics', '0003_auto_20150610_2046'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userhistory',
            options={'verbose_name_plural': 'user histories'},
        ),
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='action',
            field=models.CharField(max_length=15, choices=[(b'joined', b'Adh\xc3\xa9sion'), (b'quit', b'D\xc3\xa9mission'), (b'fired', b'Radiation'), (b'offered', b'Don')]),
        ),
    ]
