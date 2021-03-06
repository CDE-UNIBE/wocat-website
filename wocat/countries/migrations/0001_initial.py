# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-06 11:17
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'verbose_name_plural': 'Continents',
                'verbose_name': 'Continent',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False, verbose_name='code (alpha3)')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name')),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'verbose_name': 'Country',
                'ordering': ['name'],
            },
        ),
    ]
