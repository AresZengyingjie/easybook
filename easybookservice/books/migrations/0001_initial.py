# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hospital', models.CharField(max_length=20, verbose_name=b'hospital')),
                ('depart', models.CharField(max_length=10, verbose_name=b'depart')),
                ('docprof', models.CharField(max_length=10, verbose_name=b'docprof')),
                ('hosAddr', models.CharField(max_length=40, verbose_name=b'hosAddr')),
                ('time', models.CharField(max_length=10, verbose_name=b'time')),
                ('patientName', models.CharField(max_length=10, verbose_name=b'patientName')),
                ('patientID', models.CharField(max_length=20, verbose_name=b'patientID')),
                ('tel', models.CharField(max_length=50, verbose_name=b'tel')),
                ('bookID', models.CharField(max_length=500, verbose_name=b'bookID')),
                ('doc', models.ForeignKey(to='doctor.doctor')),
                ('user', models.ForeignKey(to='users.users')),
            ],
            options={
                'verbose_name': 'books',
                'verbose_name_plural': 'books',
            },
        ),
    ]
