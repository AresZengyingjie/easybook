# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('depart', '0008_depart_did'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depart',
            name='did',
        ),
        migrations.AddField(
            model_name='depart',
            name='departid',
            field=models.CharField(default=datetime.datetime(2015, 11, 23, 7, 47, 34, 493000, tzinfo=utc), max_length=10, verbose_name=b'departid'),
            preserve_default=False,
        ),
    ]
