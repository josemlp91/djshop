# -*- coding: utf-8 -*-

from django.conf.urls import url

from djshop.apps.public.views import shop
from djshop.apps.public.views import auth

urlpatterns = [
    url(r'^login/?$', auth.login, name="login"),
    url(r'^logout/?$', auth.logout, name="logout"),
    url(r'^shopping_cart/?$', shop.view_shopping_cart, name="view_shopping_cart"),
    url(r'^shopping_cart/add/?$', shop.add_to_cart, name="add_to_cart"),
    url(r'^shopping_cart/remove/?$', shop.remove_from_cart, name="remove_from_cart"),
    url(r'^shopping_cart/checkout/(?P<sale_code>[\d\w]+)/?$', shop.shopping_cart_checkout, name="shopping_cart_checkout"),
]
