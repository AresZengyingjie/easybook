# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('depart', '0007_remove_depart_did'),
    ]

    operations = [
        migrations.AddField(
            model_name='depart',
            name='did',
            field=models.CharField(default=datetime.datetime(2015, 11, 23, 7, 39, 58, 355000, tzinfo=utc), max_length=10, verbose_name=b'id'),
            preserve_default=False,
        ),
    ]
