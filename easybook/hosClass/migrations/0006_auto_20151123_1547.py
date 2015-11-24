# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosClass', '0005_hosclass_hid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hosclass',
            old_name='hid',
            new_name='hosClassid',
        ),
    ]
