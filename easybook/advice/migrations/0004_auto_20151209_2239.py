# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0003_auto_20151209_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice',
            name='disease',
            field=models.CharField(default=1, max_length=30, verbose_name=b'disease'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advice',
            name='doctor',
            field=models.CharField(default=1, max_length=10, verbose_name=b'doctor'),
            preserve_default=False,
        ),
    ]
