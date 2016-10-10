# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-05 13:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('institutions', '0004_auto_20161005_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='contact_person',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='institution_contact', to=settings.AUTH_USER_MODEL, verbose_name='Contact person'),
        ),
    ]