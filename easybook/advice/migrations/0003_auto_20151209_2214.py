# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0002_advice_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice',
            name='docAttitude',
            field=models.CharField(default=1, max_length=10, verbose_name=b'dep'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advice',
            name='recommend',
            field=models.CharField(default=1, max_length=10, verbose_name=b'dep'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advice',
            name='treatmentEffect',
            field=models.CharField(default=1, max_length=10, verbose_name=b'dep'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='advice',
            name='context',
            field=models.CharField(max_length=300, verbose_name=b'context'),
        ),
    ]
