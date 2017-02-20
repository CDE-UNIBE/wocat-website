# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-10 20:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '0027_auto_20161213_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='abstract',
            field=models.TextField(blank=True, verbose_name='Abstract'),
        ),
        migrations.AlterField(
            model_name='media',
            name='year',
            field=models.PositiveIntegerField(blank=True, default=2017, null=True, validators=[django.core.validators.MaxValueValidator(4000)], verbose_name='Year'),
        ),
    ]