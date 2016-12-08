# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-06 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20161113_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='has_update',
            field=models.BooleanField(default=False, verbose_name='是否有更新'),
        ),
        migrations.AddField(
            model_name='item',
            name='is_new',
            field=models.BooleanField(default=False, verbose_name='是否是最新'),
        ),
    ]