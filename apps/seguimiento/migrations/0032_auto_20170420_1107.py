# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-20 15:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seguimiento', '0031_auto_20170322_1009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['pk'], 'verbose_name_plural': 'items'},
        ),
        migrations.AlterModelOptions(
            name='materiales_locales',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='peticion_herramientas',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='peticion_insumos',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='peticion_maquinaria_equipo',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='peticion_materiales',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='proyecto',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='reporte_fotografico',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='reportes_avance',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='requerimiento_maq_he',
            options={'ordering': ['pk']},
        ),
        migrations.AlterModelOptions(
            name='requerimiento_personal',
            options={'ordering': ['pk']},
        ),
    ]
