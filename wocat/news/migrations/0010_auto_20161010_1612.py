# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-10 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20161010_1611'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newspage',
            old_name='country',
            new_name='countries',
        ),
    ]