# Generated by Django 2.0.2 on 2018-03-05 04:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20180304_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 5, 4, 44, 34, 711990)),
        ),
    ]