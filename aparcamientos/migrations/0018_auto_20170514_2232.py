# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0017_auto_20170514_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seleccione',
            name='nombreUsuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
