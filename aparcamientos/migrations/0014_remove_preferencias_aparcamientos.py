# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0013_auto_20170513_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preferencias',
            name='aparcamientos',
        ),
    ]
