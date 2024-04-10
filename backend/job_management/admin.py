from django.contrib import admin
from .models import *


class JobAssignmentAdmin(admin.ModelAdmin):
    list_display = [
        'mechanic',
        'job',
        'assigned_at'
        # 'is_finished'
        # 'finished_at'
    ]
class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        'mechanic',
        'date_added',
        'date_modified',
        'file_path',
        'company_name',
        'tax_identification_number',
        'invoice_number',
        'date_of_issue',
        'place_of_issue',
        'buyer',
        'email',
        'street',
        'postal_code',
        'city',
        'total',
        'iban',
        'payment_status',
        'payment_method',
    ]

class ItemAdmin(admin.ModelAdmin):
    list_display = [
        'invoice',
        'item',
        'quantity',
        'price',
        'subtotal',
    ]

admin.site.register(JobAssignment,JobAssignmentAdmin)
admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(InvoiceItem,ItemAdmin)

# Register your models here.
