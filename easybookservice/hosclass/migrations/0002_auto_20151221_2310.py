# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosclass', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hosclass',
            old_name='hosclassid',
            new_name='hosClassid',
        ),
        migrations.RemoveField(
            model_name='hosclass',
            name='hosclass',
        ),
        migrations.AddField(
            model_name='hosclass',
            name='hosClass',
            field=models.CharField(default=1, max_length=10, verbose_name=b'hosClass'),
            preserve_default=False,
        ),
    ]
