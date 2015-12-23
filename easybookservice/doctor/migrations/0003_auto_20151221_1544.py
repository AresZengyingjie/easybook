# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_doctor_docmail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='docmail',
            field=models.EmailField(max_length=254, verbose_name=b'Email'),
        ),
    ]
