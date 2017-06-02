from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^dashboard/orders$', views.showOrders, name="showOrders"),
    url(r'^products$', views.showProducts, name="showProducts"),
    url(r'^products/new$', views.newProduct, name="newProduct"),
    url(r'^products/create$', views.createProduct, name="createProduct"),
    url(r'^products/(?P<id>\d+)/edit$', views.editProduct, name="editProduct"),
    url(r'^products/update$', views.updateProduct, name="updateProduct"),
    url(r'^products/(?P<id>\d+)/destroy$', views.destroyProduct, name="destroyProduct"),
    url(r'^dashboard/orders/show/(?P<id>[0-9]+)$', views.showOrder, name="showOrder")
]
