# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Category, Product, ProductImage, InventoryItem

def index(request):
    # User.objects.create(username='admin', password='Password1')
    return render(request, 'dashboard/index.html')

def showOrders(request):
    return render(request, 'dashboard/orders.html')

def showProducts(request):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'dashboard/products.html', context )

def destroyProduct(request, id):
    Product.objects.destroyProduct( id = id )
    if 'HTTP_REFERER' in request.META:
        return redirect( request.META['HTTP_REFERER'] )
    else:
        return redirect( reverse( "db:showProducts" ) )

def showOrder(request, id):
    return render(request, 'dashboard/showOrder.html')
