# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-13 12:43
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('medialibrary', '0026_auto_20161212_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medialibrarypage',
            name='lead',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, verbose_name='Lead text'),
        ),
    ]
