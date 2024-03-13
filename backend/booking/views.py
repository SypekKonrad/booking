from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail

def index(request):

    return render(request, 'index.html')
@csrf_exempt
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


@login_required
def job_list(request):
    job_list = Job.objects.exclude(jobassignment__isnull=False)
    # print(job_list)

    return render(request, 'booking/job_list.html',
                  {'job_list': job_list})


@login_required
def customer_list(request):
    #todo ten widok docelowo bedzie usuniety
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


#todo docelowo podmieic customer_poll2 na customer_poll
def customer_poll2(request):
    form = JobForm
    if request.method == 'POST':
        print(request.POST)
        form = JobForm(request.POST)
        print("A:", form.is_valid())
        print(form.errors)
        if form.is_valid():
            job = Job.objects.create(
                first_name=form.cleaned_data['first_name'],
                surname=form.cleaned_data['surname'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                adress=form.cleaned_data['adress'],
                city=form.cleaned_data['city'],
                postal_code=form.cleaned_data['postal_code'],
                make=form.cleaned_data['make'],
                model=form.cleaned_data['model'],
                body_type=form.cleaned_data['body_type'],
                production_year=form.cleaned_data['production_year'],
                fuel_type=form.cleaned_data['fuel_type'],
                engine_displacement=form.cleaned_data['engine_displacement'],
                transmission=form.cleaned_data['transmission'],
                horsepower=form.cleaned_data['horsepower'],
                service=form.cleaned_data['service'],
            )
            return render(request,'booking/thankyou.html', {'form': form})

    return render(request,'booking/customer_poll.html', {'form': form})



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

    return render(request,'booking/customer_poll.html', {'form': form1, 'form': form2})









