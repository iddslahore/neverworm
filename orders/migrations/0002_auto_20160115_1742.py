# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 17:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='date',
        ),
        migrations.AddField(
            model_name='request',
            name='submission_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 15, 17, 42, 51, 974853, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='request',
            name='target_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
