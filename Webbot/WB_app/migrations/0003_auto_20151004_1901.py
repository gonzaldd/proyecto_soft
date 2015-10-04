# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WB_app', '0002_auto_20151004_1857'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link_archivo',
            options={'verbose_name': 'Link_archivo', 'verbose_name_plural': 'Link_archivo'},
        ),
        migrations.AlterModelOptions(
            name='publicacion',
            options={'verbose_name': 'Publicacion', 'verbose_name_plural': 'Publicacion'},
        ),
    ]
