# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('aparcamientos', '0018_auto_20170514_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencia',
            name='nombreUsuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
