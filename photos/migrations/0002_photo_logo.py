# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-09 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='logo',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]