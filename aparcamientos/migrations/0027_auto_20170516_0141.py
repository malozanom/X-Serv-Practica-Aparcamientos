# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0026_auto_20170516_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencia',
            name='colorFondo',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
