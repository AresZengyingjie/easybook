# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='disease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('diseName', models.CharField(max_length=50, verbose_name=b'diseName')),
                ('diseNamel', models.CharField(max_length=100, verbose_name=b'diseNamel')),
                ('diseSym', models.TextField(max_length=300, verbose_name=b'diseSym', blank=True)),
                ('godepart', models.CharField(max_length=30, verbose_name=b'godepart')),
                ('spread', models.CharField(max_length=30, verbose_name=b'spread')),
                ('position', models.CharField(max_length=50, verbose_name=b'spread')),
                ('highrisk', models.CharField(max_length=50, verbose_name=b'highrisk')),
            ],
            options={
                'verbose_name': 'disease',
                'verbose_name_plural': 'disease',
            },
        ),
        migrations.RemoveField(
            model_name='depart',
            name='hos',
        ),
        migrations.DeleteModel(
            name='depart',
        ),
    ]
