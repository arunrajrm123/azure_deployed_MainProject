# Generated by Django 4.2.1 on 2023-09-14 08:02

import backend.models
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_catogery_alter_useraccount_last_login_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainers',
            name='catogery',
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='last_login',
            field=backend.models.CustomDateTimeField(default=datetime.datetime(2023, 9, 14, 8, 2, 34, tzinfo=datetime.timezone.utc)),
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=50)),
                ('catogery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.catogery')),
            ],
        ),
        migrations.AddField(
            model_name='trainers',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.courses'),
        ),
    ]