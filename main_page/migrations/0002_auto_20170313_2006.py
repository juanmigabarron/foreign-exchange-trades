# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-13 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='buy_currency',
            field=models.CharField(max_length=3),
        ),
    ]