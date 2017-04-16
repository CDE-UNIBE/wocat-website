# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-07 13:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0011_auto_20170210_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='contact_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='institution_contact', to=settings.AUTH_USER_MODEL, verbose_name='Contact person'),
        ),
    ]