from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

def index(request):

    return render(request, 'index.html')

def customer_list(request):
    template = customer_list.html
    return render(request, template)

def service_detail(request):
    template = service_detail.html
    return render(request, template)

def customer_poll(request):
    if request.method == 'POST':
        form = CustomerPollForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.create(
                first_name=form.cleaned_data['first_name'],
                surname=form.cleaned_data['surname'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone number']
            )
            vehicle = Vehicle.objects.create(
                customer=customer,
                make=form.cleaned_data['make'],
                model=form.cleaned_data['make'],
                body_type=form.cleaned_data['body_type'],
                production_year=form.cleaned_data['production_year'],
                fuel_type=form.cleaned_data['fuel_type'],
                engine_displacement=form.cleaned_data['engine_displacement'],
                transmission=form.cleaned_data['transmission'],
                horsepower=form.cleaned_data['horsepower'],
                service=form.cleaned_data['service']


            )
            return render(request,'thankyou.html', {'form': form})


    else:
        form = CustomerPollForm()

    return render(request,'customer_poll.html', {'form': form})



# def vehicles(request, vehicle_id):
#     return HttpResponse("You're looking at vehicles list %s." % vehicle_id)
#
# def services(request, service_id):
#     return HttpResponse("You're looking at services list %s." % service_id)



# Create your views here.
