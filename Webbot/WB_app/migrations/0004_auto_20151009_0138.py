# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WB_app', '0003_auto_20151004_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nombre_comp_autor',
            field=models.CharField(max_length=500),
        ),
    ]
