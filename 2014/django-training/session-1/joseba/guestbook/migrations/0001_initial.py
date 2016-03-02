# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('in_time', models.DateTimeField(default=datetime.datetime(2015, 5, 26, 4, 32, 13, 221305))),
                ('out_time', models.DateTimeField(default=datetime.datetime(2015, 5, 26, 4, 32, 13, 221333))),
                ('comments', models.TextField(default=b'', null=True, blank=True)),
            ],
        ),
    ]
