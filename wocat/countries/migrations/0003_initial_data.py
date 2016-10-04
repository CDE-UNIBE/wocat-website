# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-28 11:54
from __future__ import unicode_literals

from django.db import migrations


def load_initial_coutries(apps, schema_editor):
    Country = apps.get_model('countries', 'Country')
    from django_countries import countries
    for code, name in list(countries):
        alpha3=countries.alpha3(code)
        Country.objects.create(
            code=alpha3,
            name=name,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20160928_1353'),
    ]

    operations = [
        migrations.RunPython(load_initial_coutries),
    ]