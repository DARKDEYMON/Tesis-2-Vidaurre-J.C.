# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-09 16:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0011_requerimiento_maq_he_requerimientopersonal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proyecto',
            old_name='plaso_previsto',
            new_name='plazo_previsto',
        ),
    ]