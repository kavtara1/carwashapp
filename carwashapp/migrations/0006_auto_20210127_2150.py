# Generated by Django 3.1.5 on 2021-01-27 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carwashapp', '0005_auto_20210127_1559'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discount',
            options={'verbose_name': 'Discount', 'verbose_name_plural': 'Discounts'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 27, 21, 50, 59, 252581)),
        ),
    ]
