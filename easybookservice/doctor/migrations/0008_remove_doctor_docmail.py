# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_doctor_docmail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='docmail',
        ),
    ]