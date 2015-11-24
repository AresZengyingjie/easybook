# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0006_disease_did'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='did',
            field=models.CharField(max_length=10, verbose_name=b'id'),
        ),
    ]
