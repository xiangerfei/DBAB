# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-21 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0006_auto_20180721_0458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='DBMaster2',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='\u4e3b\u6570\u636e\u5e932'),
        ),
    ]