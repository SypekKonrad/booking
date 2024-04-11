from django import forms
from . models import *
from django.forms import formset_factory, inlineformset_factory

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        # fields = '__all__'
        exclude = ['mechanic']

class InvoiceItemForm(forms.ModelForm):
    class Meta:
        model = InvoiceItem
        fields = '__all__'

InvoiceItemFormSet = inlineformset_factory(
    Invoice,  # Parent model
    InvoiceItem,  # Child model
    form=InvoiceItemForm,  # Child form
    fields='__all__',       # Include all fields from InvoiceItem
    extra=1,  # Number of extra forms to display
    can_delete=True,  # Allow deletion of extra forms
)


InvoiceFormSet = formset_factory(InvoiceForm)
ItemFormSet = formset_factory(InvoiceItemForm)