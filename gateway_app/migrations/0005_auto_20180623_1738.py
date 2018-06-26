# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-23 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gateway_app', '0004_auto_20180622_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route_map',
            name='id',
        ),
        migrations.AlterField(
            model_name='route_map',
            name='prefix',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]