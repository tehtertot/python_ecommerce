# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-31 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
