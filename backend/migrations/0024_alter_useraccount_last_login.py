# Generated by Django 4.2.1 on 2023-10-18 11:09

import backend.models
import datetime
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_subscription_amount_alter_useraccount_last_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='last_login',
            field=backend.models.CustomDateTimeField(default=datetime.datetime(2023, 10, 18, 11, 9, 15, tzinfo=datetime.timezone.utc)),
        ),
    ]
