from django.contrib.auth.models import User
from django.utils import timezone
from get_due_products import get_due_products


from shop.models import *

brand_name = "Nike"

def create_invoice_for_product(due_product: Product):
    global products
    products = get_due_products(brand_name)
    if products is None:
        pass 
        return {
            'status' : 'error',
        }
    for product in products:

        try:
            invoice = Invoice(customer=product.customer,
                description="Test", product=product,
                total_price = product.price)
            invoice.save()
        except Exception as e:
            print(e)
            print('Product not successful created')


def update_product(product: Product):

    try:
        product.previous_billing_date = timezone.now()
        product.next_billing_date = timezone.now() + timezone.timedelta(days=30)
        product.save()
        list_invoice = list(Invoice.objects.all())
        return list_invoice
        print(list_invoice)
    except Exception as e:
        print(e)
        print("Invoice Created but billing not updated")


create_invoice_for_product(brand_name)
update_product(products)
