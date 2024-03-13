from django import forms
from . models import *


class VehicleForm(forms.ModelForm):
    make = forms.CharField(label='make', max_length=20)#, error_messages={'required': 'This field is required'})
    model = forms.CharField(label='model', max_length=30)#, error_messages={'required': 'This field is required'})
    body_type = forms.CharField(label='body type', max_length=15, error_messages={'required': 'This field is required'})
    production_year = forms.IntegerField(error_messages={'required': 'This field is required'})
    fuel_type = forms.CharField(label='fuel type', max_length=20, error_messages={'required': 'This field is required'})
    engine_displacement = forms.IntegerField(error_messages={'required': 'This field is required'})
    transmission = forms.CharField(label='transmission', max_length=20, error_messages={'required': 'This field is required'})
    horsepower = forms.IntegerField(error_messages={'required': 'This field is required'})
    service = forms.CharField(label='service', widget=forms.Textarea, error_messages={'required': 'This field is required'})

    class Meta:
        model = Vehicle
        fields = ["make", "model", "body_type", "production_year", "fuel_type", "engine_displacement", "transmission", "horsepower", "service"]

class CustomerPollForm2(forms.ModelForm):
    first_name = forms.CharField(label='First name', max_length=20, error_messages={'required': 'This field is required'})
    surname = forms.CharField(label='Surname', max_length=20, error_messages={'required': 'This field is required'})
    phone_number = forms.CharField(label='phone number', max_length=9, error_messages={'required': 'This field is required'})
    email = forms.EmailField(error_messages={'required': 'This field is required'})

    class Meta:
        model = Customer
        fields = ["first_name", "surname", "phone_number", "email"]

class ContactMeForm(forms.Form):
    email = forms.EmailField(label='e-mail', max_length=20, error_messages={'required': 'This field is required'})
    subject = forms.CharField(label='subject', max_length=255, error_messages={'required': 'This field is required'})
    message = forms.CharField(widget=forms.Textarea, label='message', error_messages={'required': 'This field is required'})

class JobForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=20, error_messages={'required': 'This field is required'})
    surname = forms.CharField(label='Surname', max_length=20, error_messages={'required': 'This field is required'})
    email = forms.EmailField(label='e-mail',  error_messages={'required': 'This field is required'})
    phone_number = forms.CharField(label='phone number', max_length=9, error_messages={'required': 'This field is required'})
    adress = forms.CharField(label='Adress', max_length=20, error_messages={'required': 'This field is required'})
    city = forms.CharField(label='City', max_length=20, error_messages={'required': 'This field is required'})
    postal_code = forms.CharField(label='Postal Code', max_length=20, error_messages={'required': 'This field is required'})
    make = forms.CharField(label='Make', max_length=20)#, error_messages={'required': 'This field is required'})
    model = forms.CharField(label='Model', max_length=30)#, error_messages={'required': 'This field is required'})
    body_type = forms.CharField(label='Body Type', max_length=15, error_messages={'required': 'This field is required'})
    production_year = forms.IntegerField(label='Production Year', error_messages={'required': 'This field is required'})
    fuel_type = forms.CharField(label='Fuel Type', max_length=20, error_messages={'required': 'This field is required'})
    engine_displacement = forms.IntegerField(label='Engine Displacement', error_messages={'required': 'This field is required'})
    transmission = forms.CharField(label='Transmission', max_length=20, error_messages={'required': 'This field is required'})
    horsepower = forms.IntegerField(label='Horsepower', error_messages={'required': 'This field is required'})
    service = forms.CharField(label='Service', widget=forms.Textarea, error_messages={'required': 'This field is required'})

# class CustomerPollForm(forms.Form):
#     first_name = forms.CharField(label='First name', max_length=20, error_messages={'required': 'This field is required'})
#     surname = forms.CharField(label='Surname', max_length=20, error_messages={'required': 'This field is required'})
#     phone_number = forms.CharField(label='phone number', max_length=9, error_messages={'required': 'This field is required'})
#     email = forms.EmailField(error_messages={'required': 'This field is required'})
#     make = forms.CharField(label='make', max_length=20, error_messages={'required': 'This field is required'})
#     model = forms.CharField(label='model', max_length=30, error_messages={'required': 'This field is required'})
#     body_type = forms.CharField(label='body type', max_length=15, error_messages={'required': 'This field is required'})
#     production_year = forms.IntegerField(error_messages={'required': 'This field is required'})
#     fuel_type = forms.CharField(label='fuel type', max_length=20, error_messages={'required': 'This field is required'})
#     engine_displacement = forms.IntegerField(error_messages={'required': 'This field is required'})
#     transmission = forms.CharField(label='transmission', max_length=20, error_messages={'required': 'This field is required'})
#     horsepower = forms.IntegerField(error_messages={'required': 'This field is required'})
#     service = forms.CharField(label='service', widget=forms.Textarea, error_messages={'required': 'This field is required'})
