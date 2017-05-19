# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0034_auto_20170519_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='codigoPostal',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
