# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0022_auto_20170515_0018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preferencia',
            old_name='usuario',
            new_name='nombreUsuario',
        ),
        migrations.RenameField(
            model_name='seleccione',
            old_name='usuario',
            new_name='nombreUsuario',
        ),
    ]
