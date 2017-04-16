# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-05 08:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks
import wocat.cms.blocks
import wocat.medialibrary.blocks
import wocat.news.blocks
import wocat.users.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0054_auto_20170325_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='contact_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='project_contact', to=settings.AUTH_USER_MODEL, verbose_name='Contact person'),
        ),
    ]