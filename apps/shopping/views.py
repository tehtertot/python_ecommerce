# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from ..dashboard.models import Product, Category, Order

def index(request):
    if 'cart' not in request.session:
        request.session['cart_id'] = Order.objects.createCart()
    context = {'categories': Category.objects.all(),
               'products': Product.objects.all() }
    return render(request, 'shopping/index.html', context)

def show(request, id):
    context = {'product': Product.objects.get(id=id) }
    return render(request, 'shopping/productDetails.html', context)

def addToCart(request, id):
    if request.method == 'POST':
        postData = {'product_id': id,
                    'quantity': request.POST['quantity'],
                    'cart_id': request.session['cart_id']}
        item = Order.objects.addToCart(postData)
        if not item['status']:
            return redirect('shopping:show', id=id)
    else:
        return redirect('shopping:index')

def showCart(request):
    context = { 'cart': Order.objects.get(id=request.session['cart_id']) }
    return render(request, 'shopping/cart.html', context)
