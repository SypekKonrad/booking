import os
import pdfkit
from django.conf import settings
from django.template.loader import render_to_string, get_template


# todo co przekazać w param funkcji?
# todo update, czy oprocz data i invoice id, przekazac z modelu sciezke zapisu?
def pdf_gen(data, invoice_id):


# todo edit html invoice file for data input
    # docelowy template, moze ten zostanie
    template = get_template('docs/invoice.html')

    # data to input z html forma
    data_to_string = template.render(data)

    #plik pdf który docelowo zostanie zapisany w projekcie
    pdf_file = 'invoice_%s.pdf' % invoice_id

    pdfkit.from_string(data_to_string, os.path.join(settings.BASE_DIR, "media", pdf_file))

def calculate_total(data):
    total = 0
    for key, value in data.items():
        if 'quantity' in key:
            quantity_key = key
            price_key = key.replace('quantity', 'price')
            quantity = value
            price = data.get(price_key)
            if price is not None:
                subtotal = float(quantity) * float(price)
                total += subtotal
    return total