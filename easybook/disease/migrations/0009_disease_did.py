# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0008_remove_disease_did'),
    ]

    operations = [
        migrations.AddField(
            model_name='disease',
            name='did',
            field=models.CharField(default=datetime.datetime(2015, 11, 23, 7, 40, 2, 166000, tzinfo=utc), max_length=10, verbose_name=b'id'),
            preserve_default=False,
        ),
    ]
