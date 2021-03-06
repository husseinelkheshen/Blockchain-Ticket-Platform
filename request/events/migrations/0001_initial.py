# Generated by Django 2.0.2 on 2018-03-02 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('venues', '0002_auto_20180302_0345'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venues.Venue')),
            ],
        ),
    ]
