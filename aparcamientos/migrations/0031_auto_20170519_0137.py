# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0030_auto_20170519_0136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='accesibilidad',
            field=models.IntegerField(null=True, choices=[(0, '0'), (1, '1')]),
        ),
    ]
