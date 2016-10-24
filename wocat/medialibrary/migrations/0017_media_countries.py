# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-24 15:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0006_auto_20161024_1738'),
        ('medialibrary', '0016_remove_media_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='countries',
            field=models.ManyToManyField(blank=True, to='countries.Country', verbose_name='Countries'),
        ),
    ]
