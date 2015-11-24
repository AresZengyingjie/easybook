# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0006_remove_hospital_hid'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='hid',
            field=models.CharField(default=datetime.datetime(2015, 11, 23, 7, 40, 14, 850000, tzinfo=utc), max_length=10, verbose_name=b'id'),
            preserve_default=False,
        ),
    ]
