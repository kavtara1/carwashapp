# Generated by Django 3.1.5 on 2021-01-26 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=225, verbose_name='Name and Lastname')),
                ('employee_photo', models.ImageField(upload_to='employee_images')),
                ('personal_number', models.CharField(max_length=11, unique=True, verbose_name='Personal Number')),
                ('employee_status', models.BooleanField(default=True, verbose_name='Status')),
                ('age', models.PositiveSmallIntegerField(verbose_name='Age')),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default=1, verbose_name='Gender')),
                ('hire_date', models.DateTimeField(default=datetime.datetime(2021, 1, 27, 2, 31, 4, 768606))),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=225)),
                ('location', models.CharField(max_length=225, unique=True, verbose_name='Address')),
                ('number_of_boxes', models.PositiveSmallIntegerField(default=1, verbose_name='Number of boxes')),
                ('car_wash_image', models.ImageField(upload_to='carwash_images')),
                ('branch_employees', models.ManyToManyField(to='carwashapp.Employee')),
            ],
            options={
                'verbose_name': 'Branch',
                'verbose_name_plural': 'Branches',
            },
        ),
    ]
