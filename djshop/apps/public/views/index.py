# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render
from djshop.apps.store.models import Product


# Index view
def index(request):
    products = Product.objects.filter(is_public=True)
    replacements = {
        "products": products
    }
    return render(request, "public/index.html", replacements)
