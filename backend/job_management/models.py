from django.db import models
from accounts.models import Partner
from booking.models import Job

# class Payment
# class Invoice

class JobAssignment(models.Model):
    mechanic = models.ForeignKey(Partner, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)


