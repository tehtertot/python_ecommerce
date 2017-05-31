# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'shopping/index.html', context)

def show(request, id):
    return render(request, 'shopping/productDetails.html')

def addToCart(request, id):
    return redirect('shopping:index')

def showCart(request):
    return render(request, 'shopping/cart.html')

# testing commit
