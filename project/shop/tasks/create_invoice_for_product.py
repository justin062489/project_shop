from django.contrib.auth.models import User
from django.utils import timezone



from shop.models import *


due_products = Product.objects.filter(
    brand__brand_name='Nike',
     customer__is_active = True,
    next_billing_date__lte=timezone.now())

for due in due_products:

    try:
        invoice = Invoice(customer=due.customer, description="Test", product=due, total_price = due.price)
        invoice.save()
        due.previous_billing_date = timezone.now()
        due.next_billing_date = timezone.now() + timezone.timedelta(days=30)
        due.save()
        list_invoice = list(Invoice.objects.all())
        print(list_invoice)

    except:
        print("Invoice Creation Not Successful")


    