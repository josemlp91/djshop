# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from djshop.apps.base import views as base_views
from djshop.apps.store.forms.products import NewProductForm, EditProductForm, DeleteProductForm
from djshop.apps.store.models import Product


# List of products
@login_required
def index(request):
    products = Product.objects.all().order_by("name")
    replacements = {
        "products": products
    }
    return render(request, "store/products/index.html", replacements)


# View a product
@login_required
def view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    replacements = {
        "product": product
    }
    return render(request, "store/products/view.html", replacements)


# New product
@login_required
def new(request):
    product = Product(creator=request.user)
    return base_views.edit(request, instance=product, form_class=NewProductForm,
                           template_path="store/products/new.html", ok_url=reverse("store:view_products"))


# Edition of product
@login_required
def edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return base_views.edit(request, instance=product, form_class=EditProductForm,
                           template_path="store/products/edit.html", ok_url=reverse("store:view_products"))


# Delete a product
@login_required
def delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return base_views.delete(request, instance=product)