# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gics', '0006_auto_20150902_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='school_type',
            field=models.CharField(max_length=11, default='institution', choices=[('highschool', 'Lycée'), ('institution', 'Institution')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='person',
            name='majors',
            field=models.ManyToManyField(to='gics.Discipline', blank=True),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='action',
            field=models.CharField(max_length=15, choices=[('joined', 'Adhésion'), ('quit', 'Démission'), ('fired', 'Radiation'), ('offered', 'Don')]),
        ),
    ]
