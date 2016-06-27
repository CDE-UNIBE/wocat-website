# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='users/avatars', verbose_name='avatar'),
        ),
    ]
