# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='did',
            field=models.CharField(default=datetime.datetime(2015, 11, 23, 7, 35, 49, 876000, tzinfo=utc), unique=True, max_length=10, verbose_name=b'id'),
            preserve_default=False,
        ),
    ]
