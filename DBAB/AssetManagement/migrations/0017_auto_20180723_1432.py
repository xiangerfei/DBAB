# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-23 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0016_auto_20180723_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='VirtualIp2',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='\u865a\u62dfIP2'),
        ),
    ]
