# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aparcamientos', '0014_remove_preferencias_aparcamientos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferencia',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('colorLetra', models.CharField(max_length=50)),
                ('tamanioLetra', models.CharField(max_length=50)),
                ('colorFondo', models.CharField(max_length=50)),
                ('nombreUsuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seleccione',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombreUsuario', models.CharField(max_length=50)),
                ('FechaHora', models.DateTimeField()),
                ('aparcamiento', models.ForeignKey(to='aparcamientos.Aparcamiento')),
            ],
        ),
        migrations.RemoveField(
            model_name='preferencias',
            name='nombreUsuario',
        ),
        migrations.RemoveField(
            model_name='seleccion',
            name='aparcamiento',
        ),
        migrations.DeleteModel(
            name='Preferencias',
        ),
        migrations.DeleteModel(
            name='Seleccion',
        ),
    ]
