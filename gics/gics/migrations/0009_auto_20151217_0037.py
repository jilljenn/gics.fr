# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gics', '0008_school_picture'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='person',
            name='is_speaker',
            field=models.BooleanField(default=False),
        ),
    ]
