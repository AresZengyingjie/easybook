# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_nid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='nid',
            new_name='newsid',
        ),
    ]
