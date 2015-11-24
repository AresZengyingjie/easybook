# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disease', '0009_disease_did'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disease',
            old_name='did',
            new_name='diseaseid',
        ),
    ]
