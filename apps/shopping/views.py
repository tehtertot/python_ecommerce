# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from ..dashboard.models import Product, Category, Order

def index(request):
    context = {'categories': Category.objects.all(),
               'products': Product.objects.all() }
    return render(request, 'shopping/index.html', context)

def show(request, id):
    return render(request, 'shopping/productDetails.html')

def addToCart(request, id):
    return redirect('shopping:index')

def showCart(request):
    return render(request, 'shopping/cart.html')
