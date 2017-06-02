from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^products$', views.index),
    url(r'^products/byCat/(?P<cat_id>[0-9]+)$', views.showCategory, name="showCategory"),
    url(r'^products/orderBy$', views.setOrderBy, name="orderBy"),
    url(r'^products/(?P<id>[0-9]+)$', views.show, name="show"),
    url(r'^products/(?P<id>[0-9]+)/add$', views.addToCart, name="addToCart"),
    url(r'^products/updateCart$', views.updateCart, name="updateCart"),
    url(r'^products/cart$', views.showCart, name="showCart")
]
