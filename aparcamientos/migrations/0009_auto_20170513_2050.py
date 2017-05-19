# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0008_auto_20170513_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='orientacion',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='telefono',
            field=models.CharField(max_length=30, blank=True),
        ),
    ]
