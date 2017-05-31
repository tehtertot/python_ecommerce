# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductImage(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class InventoryItem(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Address(models.Model):
    first_name = models.CharField( max_length = 45 )
    last_name = models.CharField( max_length = 45 )
    address = models.CharField( max_length = 45 )
    address2 = models.CharField( max_length = 45 )
    city = models.CharField( max_length = 45 )
    state = models.CharField( max_length = 45 )
    zip = models.CharField( max_length = 10 )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Billing(models.Model):
    cc_num = models.CharField( max_length = 16 )
    security_code = models.CharField( max_length = 4 )
    exp_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    shipping_cost = models.DecimalField( decimal_places = 2 )
    STATUS_CHOICES = (
        ('c', 'cart'),
        ('i', 'in_process'),
        ('s', 'shipped'),
        ('x', 'cancelled'),
    )
    status = models.CharField( max_length = 1, choices = STATUS_CHOICES )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField( InventoryItem, related_name = "orders" )
    address = models.OneToOneField( Address, related_name = "order" )
    billing = models.OneToOneField( Billing, related_name = "order" )
