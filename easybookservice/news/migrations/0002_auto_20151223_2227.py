# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.CharField(default=1, max_length=100, verbose_name=b'subtitle'),
            preserve_default=False,
        ),
    ]
