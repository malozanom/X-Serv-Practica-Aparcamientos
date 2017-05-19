# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0015_auto_20170514_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencia',
            name='titulo',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
