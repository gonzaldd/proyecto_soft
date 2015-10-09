# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WB_app', '0004_auto_20151009_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='anio_publicacion',
            field=models.IntegerField(null=True),
        ),
    ]
