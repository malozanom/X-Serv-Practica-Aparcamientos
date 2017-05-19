# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0021_auto_20170515_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preferencia',
            old_name='nombreUsuario',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='seleccione',
            old_name='nombreUsuario',
            new_name='usuario',
        ),
    ]
