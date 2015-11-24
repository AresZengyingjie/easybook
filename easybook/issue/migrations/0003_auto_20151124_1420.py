# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0002_auto_20151124_1019'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='issues',
            new_name='issue',
        ),
    ]
