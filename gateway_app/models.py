# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.

class Gateway(models.Model):
    # id = models.AutoField(primary_key=True)
    gateway_name = models.CharField(max_length=100, unique=True)
    ip_addresses = ArrayField(models.GenericIPAddressField(protocol='IPv4'), blank=False)

class Route_Map(models.Model):
    # id = models.AutoField(primary_key=True)
    prefix = models.CharField(max_length=100, unique=True, primary_key=True)
    gateway = models.ForeignKey(Gateway)