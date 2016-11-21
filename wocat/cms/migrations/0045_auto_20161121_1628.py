# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-21 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0044_auto_20161121_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediasettings',
            name='facebook',
            field=models.URLField(blank=True, help_text='Your facebook page URL'),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='issuu',
            field=models.URLField(blank=True, help_text='Your issuu page URL'),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='slideshare',
            field=models.URLField(blank=True, help_text='Your slideshare page URL'),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='vimeo',
            field=models.URLField(blank=True, help_text='Your vimeo page URL'),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='youtube',
            field=models.URLField(blank=True, help_text='Your youtube page URL'),
        ),
    ]
