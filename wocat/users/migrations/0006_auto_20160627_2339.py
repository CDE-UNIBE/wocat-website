# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 21:39
from __future__ import unicode_literals

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160627_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to='users/avatars', verbose_name='avatar'),
        ),
    ]
