# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0008_auto_20151123_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='advice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dep', models.CharField(max_length=10, verbose_name=b'dep')),
                ('context', models.CharField(max_length=50, verbose_name=b'context')),
                ('tel', models.CharField(max_length=50, verbose_name=b'tel')),
                ('hos', models.ForeignKey(to='hospital.hospital')),
            ],
            options={
                'verbose_name': 'advice',
                'verbose_name_plural': 'advice',
            },
        ),
    ]
