# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-14 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_new_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='emergency_contact_information',
            field=models.TextField(blank=True, null=True, verbose_name='Emergency Contact Information'),
        ),
    ]
