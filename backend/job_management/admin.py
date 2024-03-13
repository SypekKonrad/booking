from django.contrib import admin
from .models import *


class JobAssignmentAdmin(admin.ModelAdmin):
    list_display = [
        'mechanic',
        'job',
        'assigned_at'
    ]

admin.site.register(JobAssignment,JobAssignmentAdmin)

# Register your models here.
