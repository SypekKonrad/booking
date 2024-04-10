from django.db import models
from accounts.models import Partner
from booking.models import Job
# from django.utils.translation import gettext_lazy as _

# CHOICES = (
#     ('backend', 'frontend'),
#     ('choice1', 'Choice 1'),
#     ('choice2', 'Choice 2'),
#
# )

# INVOICE_TYPE = (
#     ('vat', 'vat'),
#     ('non_vat', 'non_vat'),
# )

PAYMENT_STATUS = (
    ('paid', 'paid'),
    ('unpaid', 'unpaid'),

)

PAYMENT_METHOD = (
    ('cash', 'cash'),
    ('bank_transfer', 'bank transfer'),
    ('blik', 'blik'),
# etc

)




# class Payment
# todo jak napisze faktury to integracja jakiegoś api do płacenie i implementacja modelu płatności

class JobAssignment(models.Model):
    mechanic = models.ForeignKey(Partner, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)
    is_finished = models.BooleanField(default=False)
    finished_at = models.DateTimeField(null=True, blank=True)

class Invoice(models.Model):
    mechanic = models.ForeignKey(Partner, on_delete=models.CASCADE)
    invoice_number = models.CharField(max_length=100, verbose_name=('Invoice Number'), blank=True)



class Invoice(models.Model):
    mechanic = models.ForeignKey(Partner, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name=('Date Added'))
    date_modified = models.DateTimeField(auto_now=True, verbose_name=('Date Modified'))
    file_path = models.FileField(upload_to='media/', null=True, blank=True)
    company_name = models.CharField(max_length=100, verbose_name=('Seller'), blank=True)
    tax_identification_number = models.CharField(max_length=100, verbose_name=('Tax Identification Number'), blank=True)
    invoice_number = models.CharField(max_length=100, verbose_name=('Invoice Number'), blank=True)
    date_of_issue = models.DateTimeField(null=True, blank=True, verbose_name=('Date of Issue'))
    place_of_issue = models.CharField(max_length=100, verbose_name=('Place of Issue'), blank=True)
    buyer = models.CharField(max_length=100, verbose_name=('Buyer'), blank=True)
    email = models.EmailField(verbose_name=('Email'), blank=True)
    street = models.CharField(max_length=100, verbose_name=('Street'), blank=True)
    postal_code = models.CharField(max_length=10, verbose_name=('Postal Code'), blank=True)
    city = models.CharField(max_length=100, verbose_name=('City'), blank=True)
    total = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=('Total'))
    iban = models.CharField(max_length=100, verbose_name=('iban'), blank=True)
    payment_status = models.CharField(max_length=100, verbose_name=('Payment Status'), choices=PAYMENT_STATUS, null=True, blank=True)
    payment_method = models.CharField(max_length=100, verbose_name=('Payment Method'), choices=PAYMENT_METHOD, null=True, blank=True)

    # remarks
    # tax = models.FloatField()
    # invoice_type = models.CharField(max_length=100, verbose_name=('Invoice Type'), choices=INVOICE_TYPE, null=True, blank=True)
    #     faktura i link do platnosci bedzie wysylana mailem, tytul maila? moze jakis 1 zbiorczy
    #     message_title = models.CharField(max_length=255, verbose_name=_('Message Title'), blank=True)
    #     message_content = models.CharField(max_length=255, verbose_name=_('Message Content'), blank=True)

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    item = models.CharField(max_length=100, verbose_name=('Item'), blank=True)
    quantity = models.IntegerField(default=1, verbose_name=('Quantity'))
    price = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=('Price'))
    subtotal = models.DecimalField(max_digits=18, decimal_places=2, verbose_name=('Subtotal'))













