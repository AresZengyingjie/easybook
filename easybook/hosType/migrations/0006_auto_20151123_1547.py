# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosType', '0005_hostype_hid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostype',
            old_name='hid',
            new_name='hosTypeid',
        ),
    ]
