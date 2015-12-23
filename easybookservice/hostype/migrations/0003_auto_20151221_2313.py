# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostype', '0002_auto_20151221_2310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostype',
            old_name='hosType',
            new_name='hostype',
        ),
        migrations.RenameField(
            model_name='hostype',
            old_name='hosTypeid',
            new_name='hostypeid',
        ),
    ]
