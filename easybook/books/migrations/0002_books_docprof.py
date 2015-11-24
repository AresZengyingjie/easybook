# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='docprof',
            field=models.CharField(default=datetime.datetime(2015, 11, 23, 13, 49, 3, 29000, tzinfo=utc), max_length=10, verbose_name=b'docprof'),
            preserve_default=False,
        ),
    ]
