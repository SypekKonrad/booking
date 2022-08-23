from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
#from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
# force_text
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings





def index(request):

    return render(request, 'index.html')

@csrf_exempt
@login_required
def customer_list(request):
    customer_list = Customer.objects.all()
    for c in customer_list:
        print(c.get_display_name())
    return render(request, 'booking/customer_list.html',
                  {'customer_list': customer_list})

@login_required
@csrf_exempt
def service_detail(request, vehicle_id):
    service_detail = Vehicle.objects.get(id=vehicle_id)
    return render(request, 'booking/service_detail.html',
                  {'service_detail': service_detail})







def customer_poll(request):
    print('1')
    form1 = CustomerPollForm2
    form2 = VehicleForm

    if request.method == 'POST':
        print('2')
        print(request.POST)
        form1 = CustomerPollForm2(request.POST)
        form2 = VehicleForm(request.POST)
        print("A:", form1.is_valid(), "B:", form2.is_valid())
        print(form1.errors, form2.errors)

        if form1.is_valid() and form2.is_valid():
            customer = Customer.objects.create(
                first_name=form1.cleaned_data['first_name'],
                surname=form1.cleaned_data['surname'],
                email=form1.cleaned_data['email'],
                phone_number=form1.cleaned_data['phone_number']
            )
            print('4')
            vehicle = Vehicle.objects.create(
                customer=customer,
                make=form2.cleaned_data['make'],
                model=form2.cleaned_data['model'],
                body_type=form2.cleaned_data['body_type'],
                production_year=form2.cleaned_data['production_year'],
                fuel_type=form2.cleaned_data['fuel_type'],
                engine_displacement=form2.cleaned_data['engine_displacement'],
                transmission=form2.cleaned_data['transmission'],
                horsepower=form2.cleaned_data['horsepower'],
                service=form2.cleaned_data['service']
            )
            print('3')
            #form1.save()
            print('4')
            #form2.save()
            print('5')

            return render(request,'booking/thankyou.html', {'form1': form1, 'form2': form2})

        # else:
        #     print('6')
        #     form1 = CustomerPollForm2()
        #     form2 = VehicleForm()
            # return render(request, 'customer_poll.html', {'form1': form1, 'form2': form2})

    print('7')
    return render(request,'booking/customer_poll.html', {'form1': form1, 'form2': form2})

# def customer_poll2(request):
#     form = CustomerPollForm()
#     print('1')
#     if request.method == 'POST':
#         print('2')
#         form = CustomerPollForm(request.POST)
#         if form.is_valid():
#             print('3')
#             first_name = form.cleaned_data['first_name'],
#             surname = form.cleaned_data['surname'],
#             email = form.cleaned_data['email'],
#             phone_number = form.cleaned_data['phone_number']
#             #customer = customer
#             make = form.cleaned_data['make'],
#             model = form.cleaned_data['model'],
#             body_type = form.cleaned_data['body_type'],
#             production_year = form.cleaned_data['production_year'],
#             fuel_type = form.cleaned_data['fuel_type'],
#             engine_displacement = form.cleaned_data['engine_displacement'],
#             transmission = form.cleaned_data['transmission'],
#             horsepower = form.cleaned_data['horsepower'],
#             service = form.cleaned_data['service']
#
#             customer = Customer(
#                 first_name=first_name,
#                 surname=surname,
#                 email=email,
#                 phone_number=phone_number
#             )
#
#             vehicle = Vehicle(
#                 customer=customer,
#                 make=make,
#                 model=model,
#                 body_type=body_type,
#                 production_year=production_year,
#                 fuel_type=fuel_type,
#                 engine_displacement=engine_displacement,
#                 transmission=transmission,
#                 horsepower=horsepower,
#                 service=service
#             )
#             customer.save()
#             vehicle.save()

            # customer = Customer.objects.create(
            #     first_name=form.cleaned_data['first_name'],
            #     surname=form.cleaned_data['surname'],
            #     email=form.cleaned_data['email'],
            #     phone_number=form.cleaned_data['phone_number']
            # )
            # print('4')
            # vehicle = Vehicle.objects.create(
            #     customer=customer,
            #     make=form.cleaned_data['make'],
            #     model=form.cleaned_data['model'],
            #     body_type=form.cleaned_data['body_type'],
            #     production_year=form.cleaned_data['production_year'],
            #     fuel_type=form.cleaned_data['fuel_type'],
            #     engine_displacement=form.cleaned_data['engine_displacement'],
            #     transmission=form.cleaned_data['transmission'],
            #     horsepower=form.cleaned_data['horsepower'],
            #     service=form.cleaned_data['service']
            # )
    #         print('5')
    #         return render(request,'thankyou.html', {'form': form})
    #     else:
    #         print('6')
    #         form = CustomerPollForm()
    # print('7')
    # return render(request,'customer_poll.html', {'form': form})







