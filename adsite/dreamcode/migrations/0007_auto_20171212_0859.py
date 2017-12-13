# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-12 08:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dreamcode', '0006_auto_20171212_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='submission_template',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='contest',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 8, 59, 55, 458921, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='contest',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 12, 8, 59, 55, 458880, tzinfo=utc)),
        ),
    ]
