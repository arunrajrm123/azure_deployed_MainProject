# Generated by Django 4.2.1 on 2023-09-26 04:45

import backend.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_alter_useraccount_last_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.trainers')),
            ],
        ),
        migrations.AlterField(
            model_name='subscription',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.trainers'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_login',
            field=backend.models.CustomDateTimeField(default=datetime.datetime(2023, 9, 26, 4, 45, 19, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.appointment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
