# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='depart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departName', models.CharField(max_length=50, verbose_name=b'departName')),
                ('hos', models.ManyToManyField(to='hospital.hospital')),
            ],
            options={
                'verbose_name': 'depart',
                'verbose_name_plural': 'depart',
            },
        ),
    ]
