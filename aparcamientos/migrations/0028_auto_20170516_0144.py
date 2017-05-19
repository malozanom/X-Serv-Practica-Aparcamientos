# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0027_auto_20170516_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencia',
            name='colorFondo',
            field=models.CharField(default='fondo', max_length=50, blank=True),
            preserve_default=False,
        ),
    ]
