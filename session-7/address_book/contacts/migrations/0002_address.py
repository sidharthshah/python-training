# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_address', models.CharField(max_length=255)),
                ('building', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=6)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
