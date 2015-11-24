# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(unique=True, max_length=50, verbose_name=b'username')),
                ('password', models.CharField(max_length=15, verbose_name=b'password')),
                ('email', models.CharField(max_length=30, verbose_name=b'email')),
            ],
            options={
                'verbose_name': 'users',
                'verbose_name_plural': 'users',
            },
        ),
    ]
