# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0007_auto_20151123_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disease',
            name='did',
        ),
    ]
