# Generated by Django 2.1.1 on 2019-02-03 21:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20190203_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='daily_task_done_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 1, 22, 41, 20, 760758)),
        ),
    ]
