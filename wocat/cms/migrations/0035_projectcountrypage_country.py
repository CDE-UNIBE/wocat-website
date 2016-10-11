# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-10 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0004_country_slug'),
        ('cms', '0034_auto_20161005_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectcountrypage',
            name='country',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='countries.Country'),
            preserve_default=False,
        ),
    ]