# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2022-05-18 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(help_text='文件/文件夹名', max_length=32, verbose_name='文件夹名称'),
        ),
    ]
