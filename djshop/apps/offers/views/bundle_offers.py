# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from djshop.apps.base import views as base_views
from djshop.apps.offers.forms.bundle_offers import BundleOfferForm
from djshop.apps.offers.models import BundleOffer


# List of bundle offers
@login_required
def index(request):
    bundle_offers = BundleOffer.objects.all().order_by("name")
    replacements = {
        "bundle_offers": bundle_offers
    }
    return render(request, "offers/bundle_offers/index.html", replacements)


# View a bundle offer
@login_required
def view(request, bundle_offer_id):
    bundle_offer = get_object_or_404(BundleOffer, id=bundle_offer_id)
    replacements = {
        "bundle_offer": bundle_offer
    }
    return render(request, "offers/bundle_offers/view.html", replacements)


# New bundle offer
@login_required
def new(request):
    bundle_offer = BundleOffer(creator=request.user)
    return base_views.edit(request, instance=bundle_offer, form_class=BundleOfferForm,
                           template_path="offers/bundle_offers/new.html", ok_url=reverse("offers:view_bundle_offers"))


# Edition of bundle offer
@login_required
def edit(request, bundle_offer_id):
    bundle_offer = get_object_or_404(BundleOffer, id=bundle_offer_id)
    return base_views.edit(request, instance=bundle_offer, form_class=BundleOfferForm,
                           template_path="offers/bundle_offers/edit.html", ok_url=reverse("offers:view_bundle_offers"))


# Delete a bundle offer
@login_required
def delete(request, bundle_offer_id):
    bundle_offer = get_object_or_404(BundleOffer, id=bundle_offer_id)
    return base_views.delete(request, instance=bundle_offer)
