# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 15:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0022_auto_20161017_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte_fotografico',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
