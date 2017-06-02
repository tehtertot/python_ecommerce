# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class OrderManager(models.Manager):
    def createCart(self):
        cart = Order.objects.create(status='c')
        return cart.id
    def addToCart(self, postData):
        product = Product.objects.get(id=postData['product_id'])
        item = InventoryItem.objects.get(product=product, is_active=True)
        cart = Order.objects.get(id=postData['cart_id'])
        q = int(postData['quantity'])
        message_to_views = {}
        try:
            orderItem = cart.order_items.get(item=item)
            q = q + orderItem.quantity
            if item.num_avail < q:
                message_to_views['status'] = False
                message_to_views['info'] = "Only {} item(s) left in stock.".format(item.num_avail)
            else:
                orderItem.quantity = q
                orderItem.save()
                message_to_views['status'] = True
                message_to_views['info'] = "Added an additional {} {}(s) to your cart.".format(postData['quantity'], product.name)
        except:
            if item.num_avail < q:
                message_to_views['status'] = False
                message_to_views['info'] = "Only {} item(s) left in stock.".format(item.num_avail)
            else:
                message_to_views['status'] = True
                OrderItem.objects.create(quantity=q,order=cart,item=item)
                message_to_views['info'] = "Added {} item(s) to your cart!".format(q)
        return message_to_views
    def removeOrderItem(self, postData):
        q = OrderItem.objects.get(id=postData['orderItem']).quantity
        OrderItem.objects.get(id=postData['orderItem']).delete()
        return q
    def updateOrderItem(self, postData):
        orderitem = OrderItem.objects.get(id=postData['orderItem'])
        message_to_views = {}
        if int(postData['quantity']) > orderitem.item.num_avail:
            message_to_views['status'] = False
        else:
            q = int(postData['quantity']) - orderitem.quantity
            orderitem.quantity = postData['quantity']
            orderitem.save()
            message_to_views['status'] = True
            message_to_views['quantity'] = q
        return message_to_views

class ProductManager(models.Manager):
    def destroyProduct(self, id):
        # return self.get(id=id).delete()
        print "*"*100
        print "*** Not allowed: Product.objects.destroyProduct(...) (TODO)"
        print "*"*100

    def updateProduct(self, postData):
        print "*"*100
        print "*** Not allowed: Product.objects.updateProduct(...) (TODO)"
        print "*"*100

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProductManager()
    def getCurrentPrice(self):
        return self.items.get(product=self, is_active=True).price
    def getMainImage(self):
        return self.images.get(is_main=True)
    def getActiveInventory(self):
        return self.items.get(is_active=True)

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

class OrderItem(models.Model):
    quantity = models.PositiveSmallIntegerField()
    order = models.ForeignKey(Order, related_name = "order_items" )
    item = models.OneToOneField(InventoryItem, related_name = "order_item" )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def subtotal(self):
        return self.quantity*self.item.price
