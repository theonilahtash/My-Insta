# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-17 15:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stazone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='pub_date',
        ),
    ]
