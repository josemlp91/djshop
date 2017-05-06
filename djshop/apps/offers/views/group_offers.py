# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.decorators import permission_required, login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from djshop.apps.base import views as base_views
from djshop.apps.offers.forms.group_offers import GroupOfferForm
from djshop.apps.offers.models import GroupOffer


# List of group offers
@login_required
def index(request):
    group_offers = GroupOffer.objects.all().order_by("name")
    replacements = {
        "group_offers": group_offers
    }
    return render(request, "offers/group_offers/index.html", replacements)


# View a group offer
@login_required
def view(request, product_id):
    group_offer = get_object_or_404(GroupOffer, id=product_id)
    replacements = {
        "group_offer": group_offer
    }
    return render(request, "offers/group_offers/view.html", replacements)


# New group offer
@login_required
def new(request):
    group_offer = GroupOffer(creator=request.user)
    return base_views.edit(request, instance=group_offer, form_class=GroupOfferForm,
                           template_path="offers/group_offers/new.html", ok_url=reverse("offers:view_group_offers"))


# Edition of group offer
@login_required
def edit(request, group_offer_id):
    group_offer = get_object_or_404(GroupOffer, id=group_offer_id)
    return base_views.edit(request, instance=group_offer, form_class=GroupOfferForm,
                           template_path="offers/group_offers/edit.html", ok_url=reverse("offers:view_group_offers"))


# Delete a group offer
@login_required
def delete(request, group_offer_id):
    bundle_offer = get_object_or_404(GroupOffer, id=group_offer_id)
    return base_views.delete(request, instance=bundle_offer)
