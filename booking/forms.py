from django import forms
from . models import *




class CustomerPollForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=20)
    surname = forms.CharField(label='Surname', max_length=20)
    phone_number = forms.CharField(label='phone number', max_length=9)
    email = forms.EmailField()
    make = forms.CharField(label='make', max_length=20)
    model = forms.CharField(label='model', max_length=30)
    body_type = forms.CharField(label='body type', max_length=15)
    production_year = forms.IntegerField()
    fuel_type = forms.CharField(label='fuel type', max_length=20)
    engine_displacement = forms.IntegerField()
    transmission = forms.CharField(label='transmission', max_length=20)
    horsepower = forms.IntegerField()
    service = forms.CharField(label='service', widget=forms.Textarea)



