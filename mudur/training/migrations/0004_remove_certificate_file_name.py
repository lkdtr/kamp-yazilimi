# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-09-01 17:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0003_certificate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='file_name',
        ),
    ]
