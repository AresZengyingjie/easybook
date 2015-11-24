# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0004_remove_prof_pid'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='pid',
            field=models.CharField(default=datetime.datetime(2015, 11, 23, 7, 40, 20, 494000, tzinfo=utc), max_length=10, verbose_name=b'id'),
            preserve_default=False,
        ),
    ]
