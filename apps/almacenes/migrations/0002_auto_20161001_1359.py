# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 17:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=100)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('almacen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacenes.almacen')),
            ],
        ),
        migrations.RemoveField(
            model_name='itemsalmacen',
            name='cantidad',
        ),
        migrations.AlterField(
            model_name='itemsalmacen',
            name='tipo_item',
            field=models.CharField(choices=[('MA', 'Material'), ('He', 'Herramienta'), ('EQ', 'Equipo'), ('IN', 'Insumo')], max_length=2),
        ),
        migrations.AddField(
            model_name='inventario',
            name='itemsAlmacen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='almacenes.itemsAlmacen'),
        ),
    ]
