# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 15:51
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0009_auto_20160627_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrypage',
            name='country',
            field=django_countries.fields.CountryField(max_length=2, unique=True),
        ),
    ]