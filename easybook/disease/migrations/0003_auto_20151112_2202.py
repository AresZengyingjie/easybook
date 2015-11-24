# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0002_auto_20151112_2139'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='intro',
            field=models.TextField(max_length=500, verbose_name=b'intro', blank=True),
        ),
        migrations.AlterField(
            model_name='disease',
            name='position',
            field=models.CharField(max_length=50, verbose_name=b'position'),
        ),
    ]
