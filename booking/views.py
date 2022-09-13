from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt

def index(request):

    return render(request, 'index.html')

@csrf_exempt
@login_required
def customer_list(request):
    customer_list = Customer.objects.all()
    for c in customer_list:
        print(c.get_display_name())
    return render(request, 'customer_list.html',
                  {'customer_list': customer_list})

@login_required
@csrf_exempt
def service_detail(request, vehicle_id):
    service_detail = Vehicle.objects.get(id=vehicle_id)
    return render(request, 'service_detail.html',
                  {'service_detail': service_detail})

def customer_poll(request):
    if request.method == 'POST':
        form = CustomerPollForm(request.POST)
        if form.is_valid():
            customer = Customer.objects.create(
                first_name=form.cleaned_data['first_name'],
                surname=form.cleaned_data['surname'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number']
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


def login_view(request):
    # if request.user.is_authenticated:
    #     return render(request, '/', {})
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "login.html", context)
        login(request, user)
        return redirect('list') #csrftoken
    return render(request,"login.html", {})


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('logout')

    return render(request,"logout.html", {})



# def reqgister_view(request):
#
#     return render(request,"login.html", {})
