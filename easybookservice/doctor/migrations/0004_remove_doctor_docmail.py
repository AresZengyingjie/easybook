# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20151221_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='docmail',
        ),
    ]
