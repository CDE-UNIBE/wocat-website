# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-05 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '0024_auto_20161205_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='media',
            old_name='language',
            new_name='languages',
        ),
    ]