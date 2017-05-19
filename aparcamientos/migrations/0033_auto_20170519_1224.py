# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0032_auto_20170519_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='aparcamiento',
            name='barrio',
            field=models.CharField(default='ninguno', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='claseVial',
            field=models.CharField(default='calle', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='codigoPostal',
            field=models.PositiveSmallIntegerField(default=28994),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='coordenadaX',
            field=models.PositiveIntegerField(default=45.400452),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='coordenadaY',
            field=models.PositiveIntegerField(default=34.345435),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='distrito',
            field=models.CharField(default='ninguno', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='latitud',
            field=models.FloatField(default=45.45454),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='localidad',
            field=models.CharField(default='FUENLA', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='longitud',
            field=models.FloatField(default=5.453544),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='nombreVia',
            field=models.CharField(default='OLEEEE', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='num',
            field=models.PositiveSmallIntegerField(default=2333),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='orientacion',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='provincia',
            field=models.CharField(default='CEUTA', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='telefono',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='tipoNum',
            field=models.CharField(default='V', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='accesibilidad',
            field=models.IntegerField(choices=[(0, '0'), (1, '1')], default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='contentUrl',
            field=models.URLField(default='www.google.es', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='idEntidad',
            field=models.IntegerField(default=2131234124),
            preserve_default=False,
        ),
    ]
