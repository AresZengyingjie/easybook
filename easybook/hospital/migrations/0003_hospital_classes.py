# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_hospital_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='classes',
            field=models.CharField(default=datetime.datetime(2015, 11, 16, 14, 35, 34, 105000, tzinfo=utc), max_length=10, verbose_name=b'classes'),
            preserve_default=False,
        ),
    ]
