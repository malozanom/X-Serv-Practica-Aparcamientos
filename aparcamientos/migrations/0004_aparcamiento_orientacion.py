# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0003_usuario_contraseña'),
    ]

    operations = [
        migrations.AddField(
            model_name='aparcamiento',
            name='orientacion',
            field=models.CharField(max_length=50, default='Ninguna'),
            preserve_default=False,
        ),
    ]
