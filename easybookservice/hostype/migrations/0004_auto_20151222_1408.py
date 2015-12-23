# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostype', '0003_auto_20151221_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostype',
            name='hostype',
            field=models.CharField(max_length=10, verbose_name=b'hostype'),
        ),
    ]
