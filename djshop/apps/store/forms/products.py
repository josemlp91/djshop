# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from djshop.apps.store.models import Product
from django import forms


# Product form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "price_type", "serving_size", "min_serving_size", "max_serving_size", "main_image", "is_public", "categories"]

    class Media:
        js = ('js/store/products/form.js', )


# New product form
class NewProductForm(ProductForm):
    class Meta(ProductForm.Meta):
        model = Product
        fields = ["name", "description", "price", "price_type", "serving_size", "min_serving_size", "max_serving_size", "main_image", "is_public", "categories"]


# Edit product form
class EditProductForm(ProductForm):
    class Meta(ProductForm.Meta):
        model = Product
        fields = ["name", "description", "price", "price_type", "serving_size", "min_serving_size", "max_serving_size", "main_image", "is_public", "categories"]


# Product form
class DeleteProductForm(forms.Form):
    confirmed = forms.BooleanField(label=u"Confirm you want to delete this product")

