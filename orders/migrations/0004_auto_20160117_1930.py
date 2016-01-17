# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-17 19:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20160116_1313'),
        ('orders', '0003_auto_20160116_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(default='Nilzan 500ml', max_length=20, verbose_name='product')),
                ('submission_date', models.DateTimeField(auto_now_add=True, verbose_name='submission date')),
                ('target_date', models.DateField(default=orders.models.default_target_date, verbose_name='target date')),
                ('amount', models.IntegerField(default=0, verbose_name='amount')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Cluster')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default='0', verbose_name='quantity')),
                ('wishlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Wishlist')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Worker')),
            ],
        ),
        migrations.RemoveField(
            model_name='request',
            name='cluster',
        ),
        migrations.RemoveField(
            model_name='request',
            name='supplier',
        ),
        migrations.RemoveField(
            model_name='requestitem',
            name='request',
        ),
        migrations.RemoveField(
            model_name='requestitem',
            name='worker',
        ),
        migrations.DeleteModel(
            name='Request',
        ),
        migrations.DeleteModel(
            name='RequestItem',
        ),
    ]