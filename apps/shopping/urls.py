from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^products/(?P<id>[0-9]+)$', views.show, name="show"),
    url(r'^products/(?P<id>[0-9]+)/add$', views.addToCart, name="addToCart"),
    url(r'^products/cart$', views.showCart, name="showCart")
]
