# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-06-22 10:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gateway_app', '0002_auto_20180622_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='route_map',
            old_name='gateway_id',
            new_name='gateway',
        ),
    ]