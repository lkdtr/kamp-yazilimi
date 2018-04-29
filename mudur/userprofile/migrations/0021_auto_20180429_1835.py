# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0020_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='emergency_contact_information',
            field=models.TextField(null=True, verbose_name='Emergency Contact Information', blank=True),
        ),
    ]
