# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0005_auto_20170513_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='aparcamiento',
            field=models.ForeignKey(to='aparcamientos.Aparcamiento'),
        ),
    ]
