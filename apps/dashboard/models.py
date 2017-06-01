# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class OrderManager(models.Manager):
    def createCart(self):
        cart = Order.objects.create(status='c')
        return cart.id
    def addToCart(self, postData):
        product = Product.objects.get(id=postData['product_id'])
        item = InventoryItem.objects.filter(product=product, is_active=True)
        message_to_views = {}
        if item[0].num_avail < postData['quantity']:
            message_to_views['status'] = False
            message_to_views['info'] = "Only {} items left in stock.".format(item[0].num_avail)
        else:
            message_to_views['status'] = True
            cart = Order.objects.get(id=postData['cart_id'])
            for q in range(postData['quantity']):
                cart.items.add(item)
        return message_to_views

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProductManager(models.Manager):
    def destroyProduct(self, id):
        # return self.get(id=id).delete()
        print "*"*100
        print "*** Not allowed: Product.objects.destroyProduct(...) (TODO)"
        print "*"*100

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def getMainImage(self):
        return self.images.get(is_main=True)
    def getActiveInventory(self):
        return self.items.get(is_active=True)
    objects = ProductManager()

class ProductImage(models.Model):
    url = models.URLField()
    product = models.ForeignKey(Product, related_name="images")
    is_main = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class InventoryItem(models.Model):
    num_avail = models.IntegerField()
    num_sold = models.PositiveIntegerField()
    cost = models.DecimalField( max_digits = 10, decimal_places=2)
    price = models.DecimalField( max_digits = 10, decimal_places=2)
    is_active = models.BooleanField()
    product = models.ForeignKey(Product, related_name="items")
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
    shipping_cost = models.DecimalField(  max_digits = 10, decimal_places = 2, null = True )
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
    address = models.OneToOneField( Address, related_name = "order", null = True )
    billing = models.OneToOneField( Billing, related_name = "order", null = True )
    objects = OrderManager()
