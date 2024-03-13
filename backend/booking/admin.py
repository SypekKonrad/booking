from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'surname',
        'email'
    ]

class JobsAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'surname',
        'email',
        'phone_number',
        'adress',
        'city',
        'postal_code',
        'timestamp',
        'make',
        'model',
        'body_type',
        'production_year',
        'fuel_type',
        'engine_displacement',
        'transmission',
        'horsepower',
        'service',
    ]

admin.site.register(Job,JobsAdmin)
admin.site.register(Customer,CustomerAdmin)



# Register your models here.
