# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_remove_doctor_docmail'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='docmail',
            field=models.EmailField(default=1, max_length=254, verbose_name=b'Email'),
            preserve_default=False,
        ),
    ]
