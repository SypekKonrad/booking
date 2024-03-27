from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from job_management.models import JobAssignment
from accounts.models import Partner
from booking.models import Job
from django.utils import timezone
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



    try:
        print('3b')
        job_assignment = JobAssignment.objects.get(mechanic=partner, is_finished=False)
    except JobAssignment.DoesNotExist:
        print('4')
        if partner.active_job is None:
            
            print('none')
        # If no active job assignment is found, render a message to the frontend

        no_active_job = True
        context = {
            'no_active_job': no_active_job,
            'finished_job_assignments': finished_job_assignments,
            }
        return render(request, 'job_management/job_management.html', context)

    # job_assignment = get_object_or_404(JobAssignment, mechanic=partner)
    # job_assignment = JobAssignment.objects.filter(mechanic=partner)
    job = job_assignment.job

    
    print('3a')
    # todo musze pozwolic by 1 mechanik mógł miec kilka job assignment, ale tylko 1 active_job

    # print('finished_job_assignments', finished_job_assignments)
    # print(partner)
    # print(job_assignment)
    # print(job)

    # if partner.active_job is None:
    #     # If partner has no active job, render a message to the frontend
    #     return render(request, 'job_management/job_management.html')

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
    return render(request, 'job_management/invoice_gen.html')


@login_required
def send_mail_with_invoice(request):
    # to raczej bedzie komponent
    pass

@login_required
def pdf_gen(request):
    # samo generowanie pdfa z html template
    # to raczej bedzie komponent

    pass

def invoice_test(request):
    return render(request, 'job_management/invoice.html')
