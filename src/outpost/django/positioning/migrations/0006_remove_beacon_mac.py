# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-13 12:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("positioning", "0005_accesspoint_beacon")]

    operations = [migrations.RemoveField(model_name="beacon", name="mac")]
