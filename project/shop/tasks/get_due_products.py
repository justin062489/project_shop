from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import QuerySet
from shop.models import *


brand_name = "Nike"

def get_due_products(brand_name:str) -> QuerySet | None:
    try:
        due_products = Product.objects.filter(
            brand__brand_name = brand_name,
            customer__is_active = True,
            next_billing_date__lte=timezone.now()
        )
        return due_products
        print(due_products)
    except Exception as e:
        print(e)
        return None


get_due_products(brand_name)