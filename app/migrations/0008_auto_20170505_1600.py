# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-05 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170505_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
