# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0036_auto_20170519_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='longitud',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
