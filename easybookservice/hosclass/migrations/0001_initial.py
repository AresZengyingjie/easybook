# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hosclass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hosclassid', models.CharField(max_length=10, verbose_name=b'id')),
                ('hosclass', models.CharField(max_length=10, verbose_name=b'hosclass')),
            ],
            options={
                'verbose_name': 'hosclass',
                'verbose_name_plural': 'hosclass',
            },
        ),
    ]
