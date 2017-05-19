# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Aparcamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('idEntidad', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('accesibilidad', models.IntegerField()),
                ('contentUrl', models.URLField(max_length=300)),
                ('nombreVia', models.CharField(max_length=50)),
                ('claseVial', models.CharField(max_length=50)),
                ('tipoNum', models.CharField(max_length=10)),
                ('num', models.PositiveSmallIntegerField()),
                ('localidad', models.CharField(max_length=20)),
                ('provincia', models.CharField(max_length=20)),
                ('codigoPostal', models.PositiveSmallIntegerField()),
                ('barrio', models.CharField(max_length=30)),
                ('distrito', models.CharField(max_length=30)),
                ('coordenadaX', models.PositiveIntegerField()),
                ('coordenadaY', models.PositiveIntegerField()),
                ('latitud', models.FloatField()),
                ('longitud', models.FloatField()),
                ('telefono', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='AparcamientosMarcados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('aparcamientoId', models.IntegerField()),
                ('usuarioId', models.CharField(max_length=50)),
                ('FechaHora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('texto', models.TextField()),
                ('aparcamientoId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('colorLetra', models.CharField(max_length=50)),
                ('tamanioLetra', models.CharField(max_length=50)),
                ('colorFondo', models.CharField(max_length=50)),
                ('aparcamientos', models.ForeignKey(to='aparcamientos.AparcamientosMarcados')),
                ('identificador', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='aparcamiento',
            name='comentarios',
            field=models.ForeignKey(to='aparcamientos.Comentario'),
        ),
    ]
