# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vrp', '0002_auto_20161108_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='outputjson',
            field=models.CharField(max_length=20000),
        ),
    ]
