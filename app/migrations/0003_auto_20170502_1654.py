# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-02 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170502_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=3),
            preserve_default=False,
        ),
    ]