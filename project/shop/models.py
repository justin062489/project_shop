from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max
from django.db.models import Value
from django.db.models.functions import Replace
from django.utils import timezone
from enum import Enum


class Brand(models.Model):
    brand_name = models.CharField(max_length=200, null=True, blank=True)
    brand_code = models.CharField(max_length=120, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True,
                             default='/placeholder.png')

    def __str__(self):
        return self.brand_name

class ModelCurrency(Enum):
    USD = "US Dollars"
    PHP = "Philippine Peso"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class ModelStatus(Enum):
    active = "Active"
    terminated = "Terminated"

class Customer(models.Model):

    customer_number = models.CharField(
        primary_key=True, editable=False, max_length=100)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    brand = models.ForeignKey(
        Brand,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='Customer_brand')
    is_active = models.BooleanField(default=False)
    is_terminated = models.BooleanField(default=False)
    added_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='Customer_added_by')
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='Customer_updated_by')
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.customer_number

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def status(self):
        if self.active:
            return "Active"
        elif self.terminated:
            return "Terminated"            

    def change_status(self):
        pass
        

    def save(self, **kwargs):
        if not self.customer_number:
            max = Customer.objects.aggregate(customer_number_max=Max('customer_number'))[
                'customer_number_max']
            print(max)
            if max is not None:
                number = int(max.replace("CUSTOMER", ''))
                number += 1
            else:
                number = 1
            self.customer_number = "{}{:04d}".format('CUSTOMER',
                                                     number)
        super().save(*kwargs)


class Product(models.Model):
    product_number = models.CharField(
        primary_key=True, editable=False, max_length=100)
    currency = models.CharField(
        choices=ModelCurrency.choices(),
        max_length=20,
        blank=True,
        null=True)
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=True,
        blank=True)
    customer = models.ForeignKey(
        Customer,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='customer',
        related_name='Product_customer')
    description = models.CharField(max_length=200, null=True, blank=True)
    brand = models.ForeignKey(
        Brand,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='Product_brand')
    next_billing_date = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    previous_billing_date = models.DateTimeField(
        auto_now_add=False, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_terminated = models.BooleanField(default=False)
    added_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='Product_added_by')
    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='Product_updated_by')
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return self.product_number
    
    @property
    def status(self):
        if self.active:
            return "Active"
        elif self.terminated:
            return "Terminated"            


    def change_status(self):
        pass

    def save(self, **kwargs):
        if not self.product_number:
            max = Product.objects.aggregate(product_number_max=Max('product_number'))[
                'product_number_max']
            if max is not None:
                number = int(max.replace("PRODUCT", ''))
                number += 1
            else:
                number = 1
            self.product_number = "{}{:04d}".format('PRODUCT',
                                                    number)
        super().save(*kwargs)


class Invoice(models.Model):
    invoice_number = models.CharField(
        primary_key=True, editable=False, max_length=100)
    customer = models.ForeignKey(
        Customer,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='Invoice_customer')
    description = models.CharField(max_length=200, null=True, blank=True)
    product = models.ForeignKey(
        Product,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='Invoice_product')
    total_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.invoice_number

    def save(self, **kwargs):
        if not self.invoice_number:
            max = Invoice.objects.aggregate(invoice_number_max=Max('invoice_number'))[
                'invoice_number_max']
            if max is not None:
                number = int(max.replace("INVOICE", ''))
                number += 1
            else:
                number = 1
            self.invoice_number = "{}{:04d}".format('INVOICE',
                                                    number)
        super().save(*kwargs)
