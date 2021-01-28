from django.db import models
from datetime import datetime
from carwashapp.choises import GenderChoices, CarTypeChoices


class CompanyName(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class Branches(models.Model):
    city = models.CharField(max_length=225)
    location = models.CharField(max_length=225, unique=True, verbose_name="Address")
    number_of_boxes = models.PositiveSmallIntegerField(verbose_name="Number of boxes", default=1)
    car_wash_image = models.ImageField(upload_to='carwash_images')
    branch_employees = models.ManyToManyField(to='carwashapp.Employee', blank=False)

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.location


class Employee(models.Model):
    full_name = models.CharField(max_length=225, verbose_name="Name and Lastname")
    employee_photo = models.ImageField(upload_to='employee_images')
    personal_number = models.CharField(max_length=11, verbose_name="Personal Number", unique=True)
    employee_status = models.BooleanField(default=True, verbose_name="Status")
    age = models.PositiveSmallIntegerField(verbose_name="Age")
    gender = models.PositiveSmallIntegerField("Gender", choices=GenderChoices.choices, default=GenderChoices.Male)
    hire_date = models.DateTimeField(default=datetime.now())

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.full_name


class Prices(models.Model):
    car_type = models.PositiveSmallIntegerField("CarType", choices=CarTypeChoices.choices, default=CarTypeChoices.Sedan,
                                                unique=True)
    price = models.PositiveSmallIntegerField(verbose_name="Price")

    class Meta:
        verbose_name = "Price list"
        verbose_name_plural = "Price Lists"

    def __str__(self):
        return str(self.car_type)


class Discount(models.Model):
    prices = models.ManyToManyField(to='carwashapp.Prices', blank=False)
    discount = models.PositiveSmallIntegerField(verbose_name="discount", default=0)

    class Meta:
        verbose_name = "Discount"
        verbose_name_plural = "Discounts"

    def __str__(self):
        return f" Discount {self.discount}%"

    def prices_after_discount(self):
        discount_prices = []
        for price in self.prices.all():
            new_price = (price.price - (price.price * self.discount) / 100)
            if new_price % 1 == 0:
                discount_prices.append(int(new_price))
            else:
                discount_prices.append(new_price)
        return discount_prices
