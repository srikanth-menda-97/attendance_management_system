# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-04-16 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20180416_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Sem',
            field=models.IntegerField(),
        ),
    ]
