from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=9)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

class Vehicle(models.Model):
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    body_type = models.CharField(max_length=15)
    production_year = models.CharField(max_length=4)
    fuel_type = models.CharField(max_length=20)
    engine_displacement = models.CharField(max_length=4)
    transmission = models.CharField(max_length=20)
    horsepower = models.CharField(max_length=3)

class Service(models.Model):
    service = models.CharField(max_length=200)

# Create your models here.
