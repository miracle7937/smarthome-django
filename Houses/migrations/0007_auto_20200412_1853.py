# Generated by Django 3.0.5 on 2020-04-12 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Houses', '0006_auto_20200412_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subbreakdown',
            name='amount_paid',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 12, 18, 53, 3, 947236)),
        ),
    ]
