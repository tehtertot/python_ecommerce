# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from ..dashboard.models import Product, Category, Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    if 'cart_id' not in request.session:
        request.session['cart_id'] = Order.objects.createCart()
    all_products = Product.objects.all()
    paginator = Paginator(all_products, 15)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'categories': Category.objects.all(),
               'products': products }
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
        messages.add_message(request, messages.INFO, item['info'])
        return redirect('shopping:show', id=id)
    else:
        return redirect('shopping:index')

def showCart(request):
    cart = Order.objects.get(id=request.session['cart_id'])
    total = 0
    for item in cart.order_items.all():
        total += item.quantity*item.item.price
    context = { 'cart': cart,
                'total': total }
    return render(request, 'shopping/cart.html', context)
