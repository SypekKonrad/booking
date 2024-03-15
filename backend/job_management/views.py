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

    try:
        partner = get_object_or_404(Partner, user=request.user)
        job_assignment = get_object_or_404(JobAssignment, mechanic=partner)
        finished_job_assignments = JobAssignment.objects.filter(mechanic=partner, is_finished=True)

        job = job_assignment.job
        # print(partner)
        # print(job_assignment)
        # print(job)

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

            # elif action == 'finish':
            #     # formatted_date = now.strftime('%Y-%m-%d %H:%M:%S%z')
            #     partner.active_job = None
            #     partner.save()
            #     job_assignment.is_finished = True
            #     job_assignment.finished_at = timezone.now()
            #     job_assignment.save()
            #     return redirect('job_management')



    except Http404:
        return render(request, 'job_management/no_job_assigned.html')

    return render(request, 'job_management/job_management.html', job_context
                  #
                  )


@login_required
def job_assigned(request, id):

    try:
        job = Job.objects.get(id=id)
        partner = get_object_or_404(Partner, user=request.user)
        job_assignment = JobAssignment.objects.create(
            mechanic=partner,
            job=job
        )
        partner.active_job = job
        partner.save()

    except Http404:
        return render(request, 'job_management/job_already_assigned.html')

    return render(request, 'job_management/job_assigned.html', {'job': job})




