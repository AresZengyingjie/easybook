# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosClass', '0002_hosclass_hid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hosclass',
            name='hid',
            field=models.CharField(max_length=10, verbose_name=b'id'),
        ),
    ]
