# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-05 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0015_auto_20161005_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingresoinsumos',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='salidainsumos',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]
