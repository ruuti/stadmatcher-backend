# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-14 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_team_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='friendly',
            field=models.BooleanField(default=False),
        ),
    ]
