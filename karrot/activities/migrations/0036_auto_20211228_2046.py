# Generated by Django 3.2.9 on 2021-12-28 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0035_alter_activityparticipant_participant_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participanttype',
            name='name',
        ),
        migrations.RemoveField(
            model_name='seriesparticipanttype',
            name='name',
        ),
    ]
