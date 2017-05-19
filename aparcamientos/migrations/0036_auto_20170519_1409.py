# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0035_auto_20170519_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='latitud',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
