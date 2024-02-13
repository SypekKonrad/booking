from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

def index(request):

    return render(request, 'index.html')

def contact_me(request):
    form = ContactMeForm()
    if request.method == 'POST':
        print(request.POST)
        form = ContactMeForm(request.POST)
        print("form valid?", form.is_valid(),)
        print(form.errors)
        if form.is_valid():
            sender = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_list = [settings.EMAIL_HOST_USER, 'ksypek01@gmail.com', 'konrad.sypek@o2.pl']
            send_mail(subject, message, sender, recipient_list , fail_silently=False)
            return render(request, 'contact_me_thx.html')

    return render(request, 'contact_me.html', {'form': form})
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
    form1 = CustomerPollForm2
    form2 = VehicleForm

    if request.method == 'POST':
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


            return render(request,'booking/thankyou.html', {'form1': form1, 'form2': form2})

    return render(request,'booking/customer_poll.html', {'form1': form1, 'form2': form2})









