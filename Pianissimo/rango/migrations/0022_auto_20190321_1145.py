# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-21 11:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0021_auto_20190321_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 21, 11, 44, 59, 812513)),
        ),
    ]
