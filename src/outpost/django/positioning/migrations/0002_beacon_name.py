# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-27 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("positioning", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="beacon",
            name="name",
            field=models.CharField(
                db_index=True, default="abcd", max_length=16, unique=True
            ),
            preserve_default=False,
        )
    ]
