# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0033_auto_20170519_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='codigoPostal',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='distrito',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='latitud',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='longitud',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='num',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='orientacion',
            field=models.CharField(max_length=75, blank=True),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='telefono',
            field=models.CharField(default='S/T', max_length=40),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='tipoNum',
            field=models.CharField(max_length=10, blank=True),
        ),
    ]
