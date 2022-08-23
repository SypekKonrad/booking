from django.shortcuts import render
from django.http import HttpResponse

def index(requst):
    return HttpResponse("booking index")

def customers(request, customer_id):
    return HttpResponse("You're looking at customers list %s." % customer_id)

def vehicles(request, vehicle_id):
    return HttpResponse("You're looking at vehicles list %s." % vehicle_id)

def services(request, service_id):
    return HttpResponse("You're looking at services list %s." % service_id)

# Create your views here.
