# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-21 04:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0004_auto_20180721_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='DBMaster1',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='', max_length=200, verbose_name='\u4e3b\u6570\u636e\u5e931'),
        ),
    ]