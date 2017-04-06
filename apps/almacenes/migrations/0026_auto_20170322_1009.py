# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0025_auto_20161029_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='herramientas',
            name='decripcion',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='insumos',
            name='decripcion',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='maquinaria_equipo',
            name='decripcion',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='decripcion',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='rason_social',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='tipoactivo',
            name='tipo',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]