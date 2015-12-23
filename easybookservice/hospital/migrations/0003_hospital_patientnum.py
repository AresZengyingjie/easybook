# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_hospital_docnum'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='patientnum',
            field=models.CharField(default=0, max_length=10, verbose_name=b'patientnum'),
            preserve_default=False,
        ),
    ]
