# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aparcamientos', '0012_auto_20170513_2102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preferencias',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('titulo', models.CharField(max_length=50)),
                ('colorLetra', models.CharField(max_length=50)),
                ('tamanioLetra', models.CharField(max_length=50)),
                ('colorFondo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Seleccion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('nombreUsuario', models.CharField(max_length=50)),
                ('FechaHora', models.DateTimeField()),
                ('aparcamiento', models.ForeignKey(to='aparcamientos.Aparcamiento')),
            ],
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='aparcamientos',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.DeleteModel(
            name='AparcamientosMarcado',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='preferencias',
            name='aparcamientos',
            field=models.ForeignKey(to='aparcamientos.Seleccion'),
        ),
        migrations.AddField(
            model_name='preferencias',
            name='nombreUsuario',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
