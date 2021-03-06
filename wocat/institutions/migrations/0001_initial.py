# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-06 11:17
from __future__ import unicode_literals

import autoslug.fields
import django.core.validators
from django.db import migrations, models
import wocat.cms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
                ('abbreviation', models.CharField(max_length=255, verbose_name='Abbreviation')),
                ('url', models.URLField(blank=True, verbose_name='Url')),
                ('year', models.PositiveIntegerField(default=wocat.cms.models.get_default_year_now, validators=[django.core.validators.MaxValueValidator(4000)], verbose_name='Year')),
                ('memorandum', models.BooleanField(default=False, verbose_name='Memorandum signed')),
            ],
            options={
                'verbose_name_plural': 'Institutions',
                'ordering': ['name'],
                'verbose_name': 'Institution',
            },
        ),
    ]
