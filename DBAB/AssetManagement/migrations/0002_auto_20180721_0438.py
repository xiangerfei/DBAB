# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-21 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='HostIP',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='IP\u5730\u5740'),
        ),
    ]
