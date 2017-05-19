# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0006_auto_20170513_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='aparcamiento',
            name='telefono',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
