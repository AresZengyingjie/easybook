# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_hospital_hid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital',
            old_name='hid',
            new_name='hospitalid',
        ),
    ]
