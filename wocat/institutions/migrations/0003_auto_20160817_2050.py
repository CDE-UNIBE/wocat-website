# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('institutions', '0002_auto_20160704_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='institution',
            name='abbreviation',
            field=models.CharField(default='', max_length=255, unique=True, verbose_name='Abbreviation'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institution',
            name='country',
            field=django_countries.fields.CountryField(blank=True, max_length=2),
        ),
        migrations.AddField(
            model_name='institution',
            name='logo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Logo'),
        ),
        migrations.AddField(
            model_name='institution',
            name='url',
            field=models.URLField(blank=True, verbose_name='Url'),
        ),
    ]