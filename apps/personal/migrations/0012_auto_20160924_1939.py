# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-24 23:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0011_auto_20160924_1821'),
    ]

    operations = [
        migrations.CreateModel(
            name='designacion_cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personal.cargo')),
            ],
        ),
        migrations.RemoveField(
            model_name='designacion',
            name='cargo',
        ),
        migrations.AddField(
            model_name='designacion_cargo',
            name='designacion',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='personal.designacion'),
        ),
    ]