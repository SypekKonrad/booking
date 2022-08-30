from django import forms
from . models import *

# class PostForm(forms.ModelForm):
#     class Meta(object):
#         model = Customer
#         email = forms.Emailfield()
#         db_table =


class customer_poll(forms.Form):
    first_name = forms.CharField(label='Your name', max_length=20)
    sur_name = forms.CharField(label='Sur name', max_length=20)
    phone_number = forms.CharField(label='phone number', max_length=9)
    email = forms.EmailField()
    make = forms.CharField(label='make', max_length=20)
    model = forms.CharField(label='model', max_length=30)
    body_type = forms.CharField(label='body type', max_length=15)
    production_year = forms.CharField(label='production year', max_length=4)
    fuel_type = forms.CharField(label='fuel type', max_length=20)
    engine_displacement = forms.CharField(label='engine displacement', max_length=4)
    transmission = forms.CharField(label='transmission', max_length=20)
    horsepower = forms.CharField(label='horsepower ', max_length=3)
    service = forms.CharField(label='service', max_length=200)



