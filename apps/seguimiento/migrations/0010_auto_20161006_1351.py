# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0009_auto_20161006_1343'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='peticion_material',
            new_name='peticion_materiales',
        ),
    ]