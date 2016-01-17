# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-16 13:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160116_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='cluster',
        ),
        migrations.AddField(
            model_name='cluster',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cluster', to='users.Supplier'),
        ),
    ]
