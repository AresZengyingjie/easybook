# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosType', '0002_hostype_hid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostype',
            name='hid',
            field=models.CharField(max_length=10, verbose_name=b'id'),
        ),
    ]
