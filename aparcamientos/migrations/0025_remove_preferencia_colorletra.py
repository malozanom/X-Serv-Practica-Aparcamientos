# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0024_auto_20170515_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferencia',
            name='colorLetra',
        ),
    ]
