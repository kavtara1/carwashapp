# Generated by Django 3.1.5 on 2021-01-27 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwashapp', '0004_auto_20210127_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='prices',
        ),
        migrations.AddField(
            model_name='discount',
            name='prices',
            field=models.ManyToManyField(to='carwashapp.Prices'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 27, 15, 59, 19, 664673)),
        ),
    ]
