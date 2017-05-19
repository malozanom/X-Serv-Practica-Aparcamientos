# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0025_remove_preferencia_colorletra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencia',
            name='colorFondo',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='preferencia',
            name='tamanioLetra',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
