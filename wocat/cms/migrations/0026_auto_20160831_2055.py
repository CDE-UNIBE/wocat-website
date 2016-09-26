# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-31 18:55
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0025_regioncountry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regioncountry',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='region_countries', to='cms.RegionPage'),
        ),
    ]