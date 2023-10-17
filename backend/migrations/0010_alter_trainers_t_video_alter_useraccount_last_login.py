# Generated by Django 4.2.1 on 2023-09-15 16:11

import backend.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_video_description_video_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainers',
            name='t_video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.video'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_login',
            field=backend.models.CustomDateTimeField(default=datetime.datetime(2023, 9, 15, 16, 11, 12, tzinfo=datetime.timezone.utc)),
        ),
    ]