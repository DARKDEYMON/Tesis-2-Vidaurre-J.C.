# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-15 20:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0019_auto_20161015_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportes_avance',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]