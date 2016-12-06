# -*- coding: utf-8 -*-

from django.conf.urls import url

from djshop.apps.store.views import index
from djshop.apps.store.views import products


urlpatterns = [
    url(r'^index/?$', index.index, name="index"),

    # Products
    url(r'^products/?$', products.index, name="view_products"),
    url(r'^products/new/?$', products.new, name="new_product"),
    url(r'^products/(?P<product_id>\d+)/?$', products.view, name="view_product"),
    url(r'^products/(?P<product_id>\d+)/edit/?$', products.edit, name="edit_product"),
    url(r'^products/(?P<product_id>\d+)/delete/?$', products.delete, name="delete_product"),
]
