# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-05 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '0022_auto_20161205_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='language',
            field=models.ManyToManyField(blank=True, to='languages.Language'),
        ),
    ]
