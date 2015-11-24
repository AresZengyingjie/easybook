# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hospital',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'name')),
                ('quality', models.CharField(max_length=10, verbose_name=b'quality')),
                ('insurance', models.CharField(max_length=10, verbose_name=b'insurance')),
                ('telephone', models.CharField(max_length=20, verbose_name=b'telephone', blank=True)),
                ('address', models.CharField(max_length=200, verbose_name=b'address', blank=True)),
                ('service', models.CharField(max_length=60, verbose_name=b'service', blank=True)),
                ('summary', models.TextField(max_length=2000, verbose_name=b'summary', blank=True)),
            ],
            options={
                'verbose_name': 'hospital',
                'verbose_name_plural': 'hospital',
            },
        ),
    ]
