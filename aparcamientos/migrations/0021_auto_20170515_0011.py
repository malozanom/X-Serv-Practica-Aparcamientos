# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0020_auto_20170514_2244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seleccione',
            old_name='FechaHora',
            new_name='fechaHora',
        ),
    ]
