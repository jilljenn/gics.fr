# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('content', models.FileField(upload_to='files')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('poster', models.CharField(max_length=32, blank=True, default='')),
                ('links', models.TextField(max_length=168, blank=True, default='')),
                ('discipline', models.ManyToManyField(blank=True, to='gics.Discipline')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=64)),
                ('date', models.DateTimeField()),
                ('content', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'news',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.SlugField()),
                ('markdown', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('comments', models.TextField(null=True, blank=True)),
                ('mail', models.CharField(max_length=128)),
                ('majors', models.ManyToManyField(to='gics.Discipline')),
            ],
            options={
                'verbose_name_plural': 'people',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=64)),
                ('address', models.TextField(null=True, blank=True)),
                ('postal_code', models.CharField(null=True, max_length=5, blank=True)),
                ('city', models.CharField(null=True, max_length=32, blank=True)),
                ('manager', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateTimeField()),
                ('details', models.TextField(blank=True, default='')),
                ('slot_defined', models.BooleanField(default=False)),
                ('media_printed', models.BooleanField(default=False)),
                ('feedback_collected', models.BooleanField(default=False)),
                ('debrief_done', models.BooleanField(default=False)),
                ('lecture', models.ForeignKey(to='gics.Lecture')),
                ('school', models.ForeignKey(to='gics.School')),
                ('speaker', models.ForeignKey(to='gics.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('date', models.DateField()),
                ('action', models.CharField(choices=[('joined', 'Adhésion'), ('quit', 'Démission'), ('fired', 'Radiation'), ('offered', 'Don')], max_length=15)),
                ('donation', models.DecimalField(decimal_places=2, max_digits=16, default=0)),
                ('user', models.ForeignKey(to='gics.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('school_year', models.CharField(max_length=32)),
                ('newsletter', models.BooleanField(default=True)),
                ('school', models.ForeignKey(to='gics.School')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='person',
            name='school',
            field=models.ForeignKey(to='gics.School'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
