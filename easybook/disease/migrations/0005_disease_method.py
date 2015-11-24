# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0004_auto_20151112_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='method',
            field=models.CharField(default=datetime.datetime(2015, 11, 17, 16, 2, 18, 101000, tzinfo=utc), max_length=50, verbose_name=b'method'),
            preserve_default=False,
        ),
    ]
