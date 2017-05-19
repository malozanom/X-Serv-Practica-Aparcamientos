# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0002_auto_20170511_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='contraseña',
            field=models.CharField(default='pepe', max_length=20),
            preserve_default=False,
        ),
    ]
