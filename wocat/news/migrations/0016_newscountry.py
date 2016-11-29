# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-16 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0042_auto_20161115_1413'),
        ('news', '0015_auto_20161108_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='cms.CountryPage')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_countries', to='news.NewsPage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]