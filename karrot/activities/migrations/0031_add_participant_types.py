# Generated by Django 3.2.9 on 2021-12-20 11:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0031_activity_activities__date_5ffa2e_gist'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeriesParticipantType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('role', models.CharField(default='member', max_length=100)),
                ('max_participants', models.PositiveIntegerField(null=True)),
                ('description', models.TextField(blank=True)),
                ('activity_series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_types', to='activities.activityseries')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('role', models.CharField(default='member', max_length=100)),
                ('max_participants', models.PositiveIntegerField(null=True)),
                ('description', models.TextField(blank=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant_types', to='activities.activity')),
                ('series_participant_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participant_types', to='activities.seriesparticipanttype')),
            ],
        ),
        migrations.AddField(
            model_name='activityparticipant',
            name='participant_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.participanttype'),
        ),
    ]