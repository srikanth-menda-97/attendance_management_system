# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-04-16 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='Sem',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='attendancereport',
            name='Sem',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subject',
            name='Sem',
            field=models.IntegerField(),
        ),
    ]
