# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0003_auto_20151112_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disease',
            name='disename',
            field=models.CharField(max_length=50, verbose_name=b'disename'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='disenamel',
            field=models.CharField(max_length=100, verbose_name=b'disenamel'),
        ),
    ]
