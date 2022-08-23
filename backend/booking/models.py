from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=9, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return 'Customer ' + self.first_name
    def get_full_name(self):
        return self.first_name + "" + self.surname
    def get_display_name(self):
        return self.get_full_name()


class Vehicle(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    body_type = models.CharField(max_length=15)
    production_year = models.SmallIntegerField()
    fuel_type = models.CharField(max_length=20)
    engine_displacement = models.SmallIntegerField()
    transmission = models.CharField(max_length=20)
    horsepower = models.SmallIntegerField()
    service = models.TextField(blank=True)

class Make(models.Model):
    name = models.CharField(max_length=20)

class Model(models.Model):
    name = models.CharField(max_length=20)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)


# Create your models here.
