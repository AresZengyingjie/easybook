# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctor_did'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='did',
            field=models.CharField(max_length=10, verbose_name=b'id'),
        ),
    ]
