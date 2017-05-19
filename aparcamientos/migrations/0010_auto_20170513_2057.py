# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0009_auto_20170513_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='accesibilidad',
            field=models.IntegerField(choices=[(0, 'O'), (1, '1')]),
        ),
    ]
