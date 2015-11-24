# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depart', '0004_auto_20151112_2139'),
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docname', models.CharField(max_length=10, verbose_name=b'docname')),
                ('prof', models.CharField(max_length=20, verbose_name=b'prof')),
                ('hosp', models.CharField(max_length=30, verbose_name=b'hosp')),
                ('depa', models.CharField(max_length=20, verbose_name=b'depa')),
                ('goodat', models.TextField(max_length=100, verbose_name=b'goodat', blank=True)),
                ('time', models.CharField(max_length=15, verbose_name=b'time')),
                ('exp', models.TextField(max_length=500, verbose_name=b'exp', blank=True)),
                ('dep', models.ForeignKey(to='depart.depart')),
                ('hos', models.ForeignKey(to='hospital.hospital')),
            ],
            options={
                'verbose_name': 'doctor',
                'verbose_name_plural': 'doctor',
            },
        ),
    ]
