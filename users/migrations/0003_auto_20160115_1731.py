# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20160115_1648'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Region',
            new_name='Cluster',
        ),
        migrations.RenameField(
            model_name='village',
            old_name='region',
            new_name='cluster',
        ),
    ]
