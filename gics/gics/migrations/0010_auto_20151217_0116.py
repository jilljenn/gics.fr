# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gics', '0009_auto_20151217_0037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people', 'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='person',
            name='favorite_schools',
            field=models.ManyToManyField(related_name='favorited', to='gics.School'),
        ),
        migrations.AddField(
            model_name='person',
            name='has_priority',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.CharField(choices=[('member', 'Membre adhérent'), ('speaker', 'Simple intervenant'), ('former', 'Ancien membre ou intervenant')], default='speaker', max_length=15),
        ),
        migrations.AddField(
            model_name='userhistory',
            name='school',
            field=models.ForeignKey(to='gics.School', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='action',
            field=models.CharField(choices=[('ping', 'Contacté(e)'), ('pong', 'A répondu'), ('joined', 'Adhésion'), ('quit', 'Démission'), ('fired', 'Radiation'), ('offered', 'Don')], max_length=15),
        ),
    ]
