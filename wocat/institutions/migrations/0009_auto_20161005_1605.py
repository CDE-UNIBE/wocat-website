# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-05 14:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0008_institution_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='contact_person',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='institution_contact', to=settings.AUTH_USER_MODEL, verbose_name='Contact person'),
        ),
    ]
