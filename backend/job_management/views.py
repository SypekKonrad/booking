from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from job_management.models import JobAssignment
from accounts.models import Partner
from booking.models import Job
from django.db.utils import IntegrityError
from django.http import Http404



@login_required
def job_management(request):
    try:
        partner = get_object_or_404(Partner, user=request.user)
        job_assignment = get_object_or_404(JobAssignment, mechanic=partner)
        # job_assignment = JobAssignment.objects.filter(mechanic=partner, job=partner.active_job).first()

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
        }
        if 'submit_action' in request.POST:
            action = request.POST['submit_action']
            print('action', action)
            if action == 'cancel':
                job_assignment.delete()
                partner.active_job = None
                partner.save()
                return redirect('job_management')

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

# @login_required
# def cancel_assignment(request):
#     partner = get_object_or_404(Partner, user=request.user)
#     # print(partner)
#     # print(partner.active_job)
#     job_assignment = JobAssignment.objects.filter(mechanic=partner, job=partner.active_job).first()
#     if job_assignment:
#         job_assignment.delete()
#     # print(job_assignment)
#     partner.active_job = None
#     partner.save()
#
#     return redirect('job_management')


