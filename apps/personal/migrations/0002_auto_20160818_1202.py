# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 16:02
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_cargo', models.CharField(max_length=4, unique=True, validators=[django.core.validators.RegexValidator(code='Numero Invalido', message='El codigo de cargo es de cuatro caracteres y no contiene simbolos especiales', regex='^[0-9A-Z]{4}$')])),
                ('nombre_cargo', models.CharField(max_length=60)),
                ('salario', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='kardex',
            name='profecion',
            field=models.CharField(default='Ingeniero', max_length=40, validators=[django.core.validators.RegexValidator(code='Numero Invalido', message='La profecion deve contener solo letras', regex='[a-zA-Z]+')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='kardex',
            name='celular',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(code='Numero Invalido', message='El celular tiene un maximo de 8 dijitos', regex='^[0-9]{8}$')]),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='ci',
            field=models.CharField(max_length=9, unique=True, validators=[django.core.validators.RegexValidator(code='Numero Invalido', message='El CI Tiene un Maximo de 7 Digitos y en algunos casos dos letras mas', regex='[0-9]{7}[a-zA-Z]{0,2}')]),
        ),
        migrations.AlterField(
            model_name='kardex',
            name='telefono_fijo',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(code='Numero Invalido', message='El telefono tiene un maximo de 8 dijitos', regex='^[0-9]{7,8}$')]),
        ),
    ]
