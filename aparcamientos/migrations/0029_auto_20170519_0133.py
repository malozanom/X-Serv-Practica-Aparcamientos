# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0028_auto_20170516_0144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aparcamiento',
            name='barrio',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='claseVial',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='codigoPostal',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='coordenadaX',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='coordenadaY',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='distrito',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='email',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='latitud',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='localidad',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='longitud',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='nombreVia',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='num',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='orientacion',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='provincia',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='aparcamiento',
            name='tipoNum',
        ),
    ]
