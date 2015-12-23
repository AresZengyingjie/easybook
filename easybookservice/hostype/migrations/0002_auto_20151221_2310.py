# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostype', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostype',
            old_name='hostypeid',
            new_name='hosTypeid',
        ),
        migrations.RemoveField(
            model_name='hostype',
            name='hostype',
        ),
        migrations.AddField(
            model_name='hostype',
            name='hosType',
            field=models.CharField(default=1, max_length=10, verbose_name=b'hosType'),
            preserve_default=False,
        ),
    ]
