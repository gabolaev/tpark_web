# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-16 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0008_auto_20171213_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(default='404', max_length=15, verbose_name='Тэг'),
        ),
    ]
