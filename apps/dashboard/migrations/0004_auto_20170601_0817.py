# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 15:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20170601_0816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='dashboard.Address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='billing',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='dashboard.Billing'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]