# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0004_aparcamiento_orientacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aparcamiento',
            name='comentarios',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='aparcamientoId',
        ),
        migrations.AddField(
            model_name='comentario',
            name='aparcamiento',
            field=models.ForeignKey(to='aparcamientos.Aparcamiento', null=True),
        ),
    ]
