# Generated by Django 3.0.10 on 2020-10-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0024_make_activity_type_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitytype',
            name='name_is_default',
            field=models.BooleanField(default=True),
        ),
    ]