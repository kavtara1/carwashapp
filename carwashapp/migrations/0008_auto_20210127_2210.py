# Generated by Django 3.1.5 on 2021-01-27 18:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwashapp', '0007_auto_20210127_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='prices',
            field=models.ManyToManyField(to='carwashapp.Prices'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 27, 22, 10, 51, 441315)),
        ),
    ]