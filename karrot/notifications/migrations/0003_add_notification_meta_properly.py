# Generated by Django 3.0.2 on 2020-06-15 12:21
from datetime import datetime

from django.db import migrations, models
from pytz import utc


def migrate(apps, schema_editor):
    NotificationMeta = apps.get_model('notifications', 'NotificationMeta')
    User = apps.get_model('users', 'User')

    for user in User.objects.filter(notificationmeta__isnull=True):
        NotificationMeta.objects.create(user=user, marked_at=datetime.min.replace(tzinfo=utc))


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_add_notification_meta'),
    ]

    operations = [
        migrations.RunPython(migrate, migrations.RunPython.noop, elidable=True),
        migrations.AlterField(
            model_name='notificationmeta',
            name='marked_at',
            field=models.DateTimeField(),
        ),
    ]