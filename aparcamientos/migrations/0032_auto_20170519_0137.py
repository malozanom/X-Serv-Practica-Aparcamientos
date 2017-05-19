# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0031_auto_20170519_0137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparcamiento',
            name='contentUrl',
            field=models.URLField(null=True, max_length=300),
        ),
    ]
