# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Category, Product, ProductImage, InventoryItem
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    # User.objects.create(username='admin', password='Password1')
    return render(request, 'dashboard/index.html')

def showOrders(request):
    return render(request, 'dashboard/orders.html')

def showProducts(request):
    all_products = Product.objects.all()

    paginator = Paginator( all_products, 5 )
    page = request.GET.get( 'page' )
    try:
        products = paginator.page( page )
    except PageNotAnInteger:
        products = paginator.page( 1 )
    except EmptyPage:
        products = paginator.page( paginator.num_pages )

    context = {
        "products": products
    }
    return render(request, 'dashboard/products.html', context )

def newProduct( request ):
    context = {
        "categories": Category.objects.all(),
    }
    return render(request, 'dashboard/newProduct.html', context )

def createProduct( request ):
    pass

def editProduct(request, id):
    context = {
        "product": Product.objects.get( id = id ),
        "categories": Category.objects.all(),
    }
    return render(request, 'dashboard/editProduct.html', context )

def updateProduct(request):
    if request.method == "POST":
        Product.objects.updateProduct( request.POST )

    return redirect( reverse( "db:showProducts" ) )

def destroyProduct(request, id):
    Product.objects.destroyProduct( id = id )

    return redirect( reverse( "db:showProducts" ) )

def showOrder(request, id):
    return render(request, 'dashboard/showOrder.html')
