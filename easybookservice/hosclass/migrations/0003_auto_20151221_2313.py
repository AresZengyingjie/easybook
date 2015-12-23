# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hosclass', '0002_auto_20151221_2310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hosclass',
            old_name='hosClassid',
            new_name='hosclassid',
        ),
        migrations.RemoveField(
            model_name='hosclass',
            name='hosClass',
        ),
        migrations.AddField(
            model_name='hosclass',
            name='hosclass',
            field=models.CharField(default=1, max_length=10, verbose_name=b'hosclass'),
            preserve_default=False,
        ),
    ]
