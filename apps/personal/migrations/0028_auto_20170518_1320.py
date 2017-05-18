# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-18 17:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0027_auto_20170512_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='minnacional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minimo_nacional', models.PositiveIntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='kardex',
            name='celular',
            field=models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(code='Numero Invalido', message='El celular tiene 8 dijitos', regex='^[0-9]{8}$')]),
        ),
    ]
