# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('newsid', models.CharField(max_length=10, verbose_name=b'id')),
                ('title', models.CharField(max_length=30, verbose_name=b'title')),
                ('subtitle', models.CharField(max_length=50, verbose_name=b'subtitle')),
                ('article', models.TextField(max_length=2000, verbose_name=b'article', blank=True)),
            ],
            options={
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
            },
        ),
    ]
