# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0005_prof_pid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prof',
            old_name='pid',
            new_name='profid',
        ),
    ]
