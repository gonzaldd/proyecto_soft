# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WB_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_autor', models.AutoField(serialize=False, primary_key=True)),
                ('nombre_comp_autor', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autor',
            },
        ),
        migrations.CreateModel(
            name='Link_archivo',
            fields=[
                ('id_link', models.AutoField(serialize=False, primary_key=True)),
                ('url_link', models.CharField(max_length=200)),
                ('titulo_link', models.CharField(max_length=100)),
                ('fecha_link', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id_publicacion', models.AutoField(serialize=False, primary_key=True)),
                ('anio_publicacion', models.IntegerField()),
                ('titulo_publicacion', models.CharField(max_length=100)),
                ('cabecera_publicacion', models.CharField(max_length=300)),
                ('autores', models.ManyToManyField(to='WB_app.Autor')),
            ],
        ),
        migrations.DeleteModel(
            name='Nombre',
        ),
    ]
