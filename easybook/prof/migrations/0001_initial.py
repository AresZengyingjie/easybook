# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prof',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profName', models.CharField(max_length=10, verbose_name=b'profName')),
            ],
            options={
                'verbose_name': 'prof',
                'verbose_name_plural': 'prof',
            },
        ),
    ]
