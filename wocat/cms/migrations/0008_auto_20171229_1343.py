# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-29 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20171219_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrypage',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='countries.Country'),
        ),
    ]
