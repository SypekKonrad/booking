from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

def index(requst):
    template = loader.get_template('booking/index.html')
    return render(request, template)

def customer_list(request):
    template = customer_list.html
    return render(request, template)

def customer_vehicle(request):
    template = customer_vehicle.html
    return render(request, template)

def service_detail(request):
    template = service_detail.html
    return render(request, template)

def customer_poll(request):
    if request.method == 'POST':
        form = customer_poll(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/RandomAfterDataEntryTemplate/') #dorobic cos do przekierowania

    else:
        form = customer_poll()

    return render(request,'customer_poll.html', {'form': form})

# def vehicles(request, vehicle_id):
#     return HttpResponse("You're looking at vehicles list %s." % vehicle_id)
#
# def services(request, service_id):
#     return HttpResponse("You're looking at services list %s." % service_id)



# Create your views here.
