# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depart', '0005_depart_did'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depart',
            name='did',
            field=models.CharField(max_length=10, verbose_name=b'id'),
        ),
    ]
