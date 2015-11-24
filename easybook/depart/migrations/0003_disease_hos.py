# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
        ('depart', '0002_auto_20151112_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='hos',
            field=models.ManyToManyField(to='hospital.hospital'),
        ),
    ]
