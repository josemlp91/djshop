# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from djshop.apps.offers.models import BundleOffer
from django import forms


# Bundle offer form
class BundleOfferForm(forms.ModelForm):
    class Meta:
        model = BundleOffer
        fields = ["name", "description", "product", "bundle_product_units", "paid_product_units"]


# Product form
class DeleteBundleOfferForm(forms.Form):
    confirmed = forms.BooleanField(label=u"Confirm you want to delete this offer")
