# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 01:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviestrailer_cover_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviestrailer',
            name='cover_image_url',
            field=models.CharField(max_length=200),
        ),
    ]