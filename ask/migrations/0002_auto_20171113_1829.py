# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.IntegerField(default=0, verbose_name='rate of user'),
        ),
        migrations.AddField(
            model_name='user',
            name='upload',
            field=models.ImageField(default='/ask/static/avatars/emptyUser.png', upload_to='uploads/%Y/%m/%d/'),
        ),
    ]
