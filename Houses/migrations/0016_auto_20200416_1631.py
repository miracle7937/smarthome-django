# Generated by Django 3.0.5 on 2020-04-16 15:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Houses', '0015_auto_20200416_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subbreakdown',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 16, 31, 17, 894735)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 16, 31, 17, 893736)),
        ),
        migrations.AlterField(
            model_name='tour',
            name='dateOfTour',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 16, 16, 31, 17, 894735)),
        ),
    ]
