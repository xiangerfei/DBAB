# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-21 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManagement', '0010_auto_20180721_0728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='DBComment',
            field=models.CharField(max_length=20, verbose_name='DB\u5f52\u5c5e\u4e1a\u52a1'),
        ),
    ]