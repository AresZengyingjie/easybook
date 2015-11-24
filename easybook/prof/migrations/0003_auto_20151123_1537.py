# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0002_prof_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prof',
            name='pid',
            field=models.CharField(max_length=10, verbose_name=b'id'),
        ),
    ]
