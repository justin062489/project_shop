from django.contrib.auth.models import User
from django.utils import timezone


from shop.models import *


due_product = Product.objects.get(product_number = 'PRODUCT0009')


try:
    invoice = Invoice(customer=due_product.customer, description="Test", product=due_product, total_price = due_product.price)
    invoice.save()
    due_product.previous_billing_date = timezone.now()
    due_product.next_billing_date = timezone.now() + timezone.timedelta(days=30)
    due_product.save()
    list_invoice = list(Invoice.objects.all())
    print(list_invoice)

except:
    print("Invoice Creation Not Successful")


    