# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('guestbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logentry',
            options={'verbose_name': 'Johl!', 'verbose_name_plural': 'Johlies!'},
        ),
        migrations.AlterField(
            model_name='logentry',
            name='in_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 4, 45, 37, 870529)),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='out_time',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 26, 4, 45, 37, 870557)),
        ),
    ]
