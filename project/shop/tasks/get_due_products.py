from django.contrib.auth.models import User
from django.utils import timezone


from shop.models import *


due_products = Product.objects.filter(
    brand__brand_name='Nike',
    customer__status='Active',
    next_billing_date__lte=timezone.now())
print(due_products)
