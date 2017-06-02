# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from ..dashboard.models import Product, Category, Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    if 'cart_id' not in request.session:
        request.session['cart_id'] = Order.objects.createCart()
        request.session['cart_items'] = 0
        request.session['orderBy'] = 'name'
    request.session['category_id'] = 0
    all_products = Product.objects.all().order_by(request.session['orderBy'])
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

def setOrderBy(request):
    if request.method == "POST":
        if request.POST['sort_by'] == 'price':
            request.session['orderBy'] = 'items__price'
            print request.session['orderBy']
        elif request.POST['sort_by'] == 'popularity':
            request.session['orderBy'] = '-items__num_sold'
        else:
            request.session['orderBy'] = request.POST['sort_by']
        if request.session['category_id'] == 0:
            return redirect('shopping:index')
        else:
            return redirect('shopping:showCategory', request.session['category_id'])

def showCategory(request, cat_id):
    request.session['category_id'] = cat_id
    cat = Category.objects.get(id=cat_id)
    cat_products = Product.objects.filter(category=cat).order_by(request.session['orderBy'])
    paginator = Paginator(cat_products, 15)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'categories': Category.objects.all(),
               'products': products,
               'category': cat }
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
        if item['status']:
            request.session['cart_items'] += int(request.POST['quantity'])
        return redirect('shopping:show', id=id)
    else:
        return redirect('shopping:index')

def updateCart(request):
    if request.method == "POST":
        if request.POST['quantity'] == "0":
            request.session['cart_items'] -= Order.objects.removeOrderItem(request.POST)
            return redirect('shopping:showCart')
        else:
            update = Order.objects.updateOrderItem(request.POST)
            if not update['status']:
                messages.add_message(request, messages.ERROR, "not enough inventory available")
            else:
                request.session['cart_items'] += update['quantity']
        return redirect('shopping:showCart')

def showCart(request):
    cart = Order.objects.get(id=request.session['cart_id'])
    total = 0
    for item in cart.order_items.all():
        total += item.quantity*item.item.price
    context = { 'cart': cart,
                'total': total }
    return render(request, 'shopping/cart.html', context)

def populateProducts(request):
    if request.session['category_id'] == 0:
        cat = ""
        products = Product.objects.all().order_by(request.session['orderBy'])
    else:
        cat = Category.objects.get(id=request.session['category_id'])
        products = Product.objects.filter(category=cat).order_by(request.session['orderBy'])
    paginator = Paginator(products, 15)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return products
