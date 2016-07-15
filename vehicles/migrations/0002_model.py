# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 03:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('C', 'Carro'), ('M', 'Moto')], max_length=1, verbose_name='tipo')),
                ('name', models.CharField(max_length=60, verbose_name='nome')),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.Manufacturer', verbose_name='montadora')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos',
                'ordering': ['name'],
            },
        ),
    ]
