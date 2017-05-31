# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    # User.objects.create(username='admin', password='Password1')
    return render(request, 'dashboard/index.html')

def showOrders(request):
    return render(request, 'dashboard/orders.html')

def showProducts(request):
    return render(request, 'dashboard/products.html')

def showOrder(request, id):
    return render(request, 'dashboard/showOrder.html')
