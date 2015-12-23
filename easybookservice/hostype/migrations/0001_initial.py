# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hostype',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostypeid', models.CharField(max_length=10, verbose_name=b'id')),
                ('hostype', models.CharField(max_length=10, verbose_name=b'hostype')),
            ],
            options={
                'verbose_name': 'hostype',
                'verbose_name_plural': 'hostype',
            },
        ),
    ]
