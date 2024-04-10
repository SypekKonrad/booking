from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from job_management.models import JobAssignment, InvoiceItem, Invoice
from accounts.models import Partner
from booking.models import Job
from django.utils import timezone
from job_management.forms import InvoiceForm, InvoiceItemForm, InvoiceFormSet, ItemFormSet, InvoiceItemFormSet
from django.db.utils import IntegrityError
from django.http import Http404
from datetime import datetime
from datetime import date
import time
import pytz


@login_required
def job_management(request):

    print('1')
    partner = get_object_or_404(Partner, user=request.user)
    print('2')
    finished_job_assignments = JobAssignment.objects.filter(mechanic=partner, is_finished=True)
    finished_jobs = [assignment.job for assignment in finished_job_assignments]
    for job in finished_jobs:
        print(job.first_name)
        print(job.surname)


    try:
        print('3b')
        job_assignment = JobAssignment.objects.get(mechanic=partner, is_finished=False)

    except JobAssignment.DoesNotExist:
        print('4')
        if partner.active_job is None:
            print('none')

        no_active_job = True
        context = {
            'no_active_job': no_active_job,
            'finished_job_assignments': finished_job_assignments,
            'finished_jobs': finished_jobs,
            }
        return render(request, 'job_management/job_management.html', context)

    job = job_assignment.job   

    job_context = {
        'first_name': job.first_name,
        'surname': job.surname,
        'email': job.email,
        'phone_number': job.phone_number,
        'adress': job.adress,
        'city': job.city,
        'postal_code': job.postal_code,
        'timestamp': job.timestamp,
        'make': job.make,
        'model': job.model,
        'body_type': job.body_type,
        'production_year': job.production_year,
        'fuel_type': job.fuel_type,
        'engine_displacement': job.engine_displacement,
        'transmission': job.transmission,
        'horsepower': job.horsepower,
        'service': job.service,
        'finished_job_assignments': finished_job_assignments,
        'finished_jobs': finished_jobs,
        # 'id': job.id,

    }
    if 'submit_action' in request.POST:
        action = request.POST['submit_action']
        print(request.POST)
        print('action:', action)

        if action == 'cancel':
            job_assignment.delete()
            partner.active_job = None
            partner.save()
            return redirect('job_management')

        elif action == 'finish':
            # formatted_date = now.strftime('%Y-%m-%d %H:%M:%S%z')
            partner.active_job = None
            partner.save()
            job_assignment.is_finished = True
            job_assignment.finished_at = timezone.now()
            job_assignment.save()
            return redirect('job_management')

    return render(request, 'job_management/job_management.html', job_context
                  #
                  )


@login_required
def job_details(request, id):
    job = Job.objects.get(id=id)
    return render(request, 'job_management/job_details.html', {'job': job})


@login_required
def job_assigned(request, id):

    # try:
    job = Job.objects.get(id=id)
    partner = get_object_or_404(Partner, user=request.user)
# todo musze pozwolic by 1 mechanik mógł miec kilka job assignment, ale tylko 1 active_job
    if partner.active_job is not None:
        return render(request, 'job_management/job_already_assigned.html')
    
    job_assignment = JobAssignment.objects.create(
        mechanic=partner,
        job=job
    )
    partner.active_job = job
    partner.save()

    # except Http404:
    #     return render(request, 'job_management/job_already_assigned.html')

    return render(request, 'job_management/job_assigned.html', {'job': job})



@login_required
def invoice_management_panel(request):
    # zbiorczy widok z fakturami
    # filter by user/mechanic
    # invoices = Invoice.objects.filter()

    return render(request, 'job_management/invoice_management_panel.html')
#, {'invoices': invoices})


@login_required
def invoice_gen(request):
    # zbieranie danych z forma
    # for form in formset:
    #     print(form)
    # print(item_formset)

    invoice_form = InvoiceForm
    item_formset = InvoiceItemFormSet

    render_context = {

        'invoice_form': invoice_form,
        'item_formset': item_formset,
    }

    if request.method == 'POST':
        print(request.POST)
        invoice_form = InvoiceForm(request.POST)
        item_formset = InvoiceItemFormSet(request.POST)

        print("invoice form valid:", invoice_form.is_valid(), ",", "item formset valid:", item_formset.is_valid())
        print("invoice form errors:", invoice_form.errors, "item formset errors:", item_formset.errors)

        post_context = {
            'invoice_form': invoice_form,
            'item_formset': item_formset,
        }

        if invoice_form.is_valid() and item_formset.is_valid():

            item = InvoiceItem.objects.create(
                invoice=item_formset.cleaned_data['first_name'],
                item=item_formset.cleaned_data['first_name'],
                quantity=item_formset.cleaned_data['first_name'],
                price=item_formset.cleaned_data['first_name'],
                subtotal=item_formset.cleaned_data['first_name'],
            )

            invoice = Invoice.objects.create(
                mechanic=invoice_form.cleaned_data['first_name'], # lol to request user
                date_adde=invoice_form.cleaned_data['first_name'], # jakis datetime.now
                date_modified=invoice_form.cleaned_data['first_name'],# jakis datetime.now
                file_path=invoice_form.cleaned_data['first_name'], # tu jeszcze nie wiem
                company_name=invoice_form.cleaned_data['first_name'],
                tax_identification_number=invoice_form.cleaned_data['first_name'],
                invoice_number=invoice_form.cleaned_data['first_name'],
                date_of_issue=invoice_form.cleaned_data['first_name'],
                place_of_issue=invoice_form.cleaned_data['first_name'],
                buyer=invoice_form.cleaned_data['first_name'],
                email=invoice_form.cleaned_data['first_name'],
                street=invoice_form.cleaned_data['first_name'],
                postal_code=invoice_form.cleaned_data['first_name'],
                city=invoice_form.cleaned_data['first_name'],
                total=invoice_form.cleaned_data['first_name'],
                iban=invoice_form.cleaned_data['first_name'],
                payment_status=invoice_form.cleaned_data['first_name'],
                payment_method=invoice_form.cleaned_data['first_name'],
            )




        # todo dopasować do gałęzi ifa/ten return wykona render po tym jak form przejdzie
        return render(request, 'job_management/invoice_gen.html', post_context)

    # tu musze przekazac form i formset, to jest render po zaladowaniu /invoices/new/
    return render(request, 'job_management/invoice_gen.html', render_context)


def send_mail_with_invoice():
    # to raczej bedzie komponent
    pass

def pdf_gen():

    # samo generowanie pdfa z html template
    # to raczej bedzie komponent

    pass

def invoice_test(request):
    return render(request, 'job_management/invoice.html')
