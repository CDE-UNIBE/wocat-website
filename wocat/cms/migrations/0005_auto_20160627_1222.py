# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-27 10:22
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wocat.cms.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20160622_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='header',
            field=wagtail.wagtailcore.fields.StreamField((('carousel', wagtail.wagtailcore.blocks.StructBlock((('images', wagtail.wagtailcore.blocks.ListBlock(wocat.cms.blocks.ImageBlock())), ('heading', wagtail.wagtailcore.blocks.CharBlock()), ('content', wocat.cms.blocks.RichTextBlock(required=False))))),), blank=True),
        ),
    ]