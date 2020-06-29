# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 09:43
from __future__ import unicode_literals

from django.db import migrations
from django.db.models import Q


def convert_comment_to_description(apps, schema_editor):
    history_model = apps.get_model('history', 'History')

    # convert
    for h in history_model.objects.filter(payload__has_key='comment'):
        h.payload['description'] = h.payload['comment']
        del h.payload['comment']
        h.save()

    for h in history_model.objects.filter(payload__has_key='is_comment_changed'):
        h.payload['is_description_changed'] = h.payload['is_comment_changed']
        del h.payload['is_comment_changed']
        h.save()

    # check
    assert history_model.objects.\
        filter(Q(payload__has_key='comment') | Q(payload__has_key='is_comment_changed')).\
        count() == 0


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0005_auto_20181114_1126'),
        ('places', '0014_activityseries_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='comment',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='is_comment_changed',
            new_name='is_description_changed',
        ),
        migrations.RenameField(
            model_name='activityseries',
            old_name='comment',
            new_name='description',
        ),
        migrations.RunPython(convert_comment_to_description, elidable=True)
    ]
