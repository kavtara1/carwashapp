from django.db import models
from datetime import datetime
from carwashapp.choises import GenderChoices


class CompanyName(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Branches(models.Model):
    city = models.CharField(max_length=225)
    location = models.CharField(max_length=225, unique=True, verbose_name="Address")
    number_of_boxes = models.PositiveSmallIntegerField(verbose_name="Number of boxes", default=1)
    CarWashImage = models.ImageField()

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.location


class Employee(models.Model):
    full_name = models.CharField(max_length=225, verbose_name="Name and Lastname")
    employee_photo = models.ImageField()
    personal_number = models.CharField(max_length=11, verbose_name="Personal Number", unique=True)
    employee_status = models.BooleanField(default=True, verbose_name="Status")
    age = models.PositiveSmallIntegerField(verbose_name="Age")
    working_location = models.OneToOneField(to="carwashapp.Branches", on_delete=models.PROTECT, related_name="employee")
    gender = models.PositiveSmallIntegerField("Gender", choices=GenderChoices.choices, default=GenderChoices.Male)
    hire_date = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.full_name







