# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 15:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0021_auto_20161016_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reporte_fotografico',
            old_name='curriculum',
            new_name='fotos_reporte',
        ),
    ]