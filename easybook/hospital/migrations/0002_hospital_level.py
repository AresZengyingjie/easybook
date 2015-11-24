# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='level',
            field=models.CharField(default=datetime.datetime(2015, 11, 16, 13, 56, 12, 967000, tzinfo=utc), max_length=10, verbose_name=b'level'),
            preserve_default=False,
        ),
    ]
