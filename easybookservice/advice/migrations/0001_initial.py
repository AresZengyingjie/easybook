# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='advice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recommend', models.CharField(max_length=10, verbose_name=b'dep')),
                ('treatmentEffect', models.CharField(max_length=10, verbose_name=b'dep')),
                ('disease', models.CharField(max_length=30, verbose_name=b'disease')),
                ('doctor', models.CharField(max_length=10, verbose_name=b'doctor')),
                ('docAttitude', models.CharField(max_length=10, verbose_name=b'dep')),
                ('dep', models.CharField(max_length=10, verbose_name=b'dep')),
                ('context', models.CharField(max_length=300, verbose_name=b'context')),
                ('tel', models.CharField(max_length=50, verbose_name=b'tel')),
                ('hos', models.ForeignKey(to='hospital.hospital')),
                ('user', models.ForeignKey(to='users.users')),
            ],
            options={
                'verbose_name': 'advice',
                'verbose_name_plural': 'advice',
            },
        ),
    ]
