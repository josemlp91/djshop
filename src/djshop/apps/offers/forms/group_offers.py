# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.core.exceptions import ValidationError

from djshop.apps.offers.models import GroupOffer
from django import forms


# Bundle offer form
class GroupOfferForm(forms.ModelForm):
    class Meta:
        model = GroupOffer
        fields = ["name", "description", "discount_amount", "discount_type", "product_categories", "products"]

    def clean(self):
        cleaned_data = super(GroupOfferForm, self).clean()
        if not cleaned_data.get("product_categories") and not cleaned_data.get("product_categories"):
            raise ValidationError(u"You must select at least one product category or product")
        return cleaned_data


# Product form
class DeleteGroupOfferForm(forms.Form):
    confirmed = forms.BooleanField(label=u"Confirm you want to delete this offer")
