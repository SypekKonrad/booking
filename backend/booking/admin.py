from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'surname',
        'email'
    ]

admin.site.register(Customer,CustomerAdmin)



# Register your models here.
