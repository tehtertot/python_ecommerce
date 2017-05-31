from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^dashboard/orders$', views.showOrders, name="showOrders"),
    url(r'^dashboard/products$', views.showProducts, name="showProducts"),
    url(r'^dashboard/orders/show/(?P<id>[0-9]+)$', views.showOrder, name="showOrder")
]
