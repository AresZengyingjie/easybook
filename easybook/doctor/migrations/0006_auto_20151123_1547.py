# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_doctor_did'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='did',
            new_name='doctorid',
        ),
    ]
