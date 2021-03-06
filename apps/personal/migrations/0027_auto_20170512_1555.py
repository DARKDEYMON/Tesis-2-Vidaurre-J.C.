# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 19:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0026_auto_20170322_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='nombre_cargo',
            field=models.CharField(max_length=60, validators=[django.core.validators.RegexValidator(code='Numero Invalido', message='El cargo deve contener solo letras y un minimo de dos caracteres', regex='^(([a-zA-Z]{2,} )||([a-zA-Z]{2,}))+$')]),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='profesion',
            field=models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(code='Numero Invalido', message='La profecion deve contener solo letras', regex='^[a-zA-Z]{3,}$')]),
        ),
    ]
