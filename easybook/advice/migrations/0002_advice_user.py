# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('advice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice',
            name='user',
            field=models.ForeignKey(default=1, to='users.users'),
            preserve_default=False,
        ),
    ]
