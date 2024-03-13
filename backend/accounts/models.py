from django.contrib.auth.models import User
from django.db import models
from booking.models import Job


class Partner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    active_job = models.OneToOneField(Job, on_delete=models.CASCADE, default=None, null=True)


    def __str__(self):
        return self.company_name


