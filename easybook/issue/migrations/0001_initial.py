# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='issue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issueid', models.CharField(max_length=5, verbose_name=b'issueid')),
                ('issuename', models.CharField(max_length=10, verbose_name=b'issuename')),
                ('issuecontent', models.TextField(max_length=4000, verbose_name=b'issuecontent')),
            ],
            options={
                'verbose_name': 'issue',
                'verbose_name_plural': 'issue',
            },
        ),
    ]
