# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_activity_notifications_sent'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='upcoming_notification_hours',
            field=models.PositiveIntegerField(default=4),
        ),
    ]
