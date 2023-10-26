from .models import Invoice, InvoiceItem, Product
from math import floor

def invoice_builder(username, items):
    invoice = {'username': username}
    invoice = Invoice.objects.create(username=username, amount=0.0)
    amount = 0.0
    for item in items:
        product = Product.objects.get(id=item['product'])
        invoice_item = InvoiceItem.objects.create(invoice=invoice,
                            name=product.name, price=product.price,
                            quantity=item['quantity'])
        amount += product.price * item['quantity']
        invoice.items.add(invoice_item)
    result = float("{:.2f}".format(amount))
    invoice.amount = result
    return invoice
