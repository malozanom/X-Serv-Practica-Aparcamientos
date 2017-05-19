# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0029_auto_20170519_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='idEntidad',
            field=models.IntegerField(null=True),
        ),
    ]
