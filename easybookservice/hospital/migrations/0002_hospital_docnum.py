# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='docnum',
            field=models.CharField(default=12, max_length=10, verbose_name=b'docnum'),
            preserve_default=False,
        ),
    ]
