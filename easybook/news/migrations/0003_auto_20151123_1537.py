# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_nid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='nid',
            field=models.CharField(max_length=10, verbose_name=b'id'),
        ),
    ]
