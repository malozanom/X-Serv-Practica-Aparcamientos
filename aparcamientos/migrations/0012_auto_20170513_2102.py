# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0011_auto_20170513_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='identificador',
            new_name='nombre',
        ),
    ]
