# -*- coding: utf-8 -*-

from django.conf.urls import url

from djshop.apps.offers.views import index
from djshop.apps.offers.views import bundle_offers
from djshop.apps.offers.views import group_offers


urlpatterns = [
    url(r'^$', index.index, name="index"),

    # Bundle offers
    url(r'^bundle_offers/?$', bundle_offers.index, name="view_bundle_offers"),
    url(r'^bundle_offers/new/?$', bundle_offers.new, name="new_bundle_offer"),
    url(r'^bundle_offers/(?P<bundle_offer_id>\d+)/?$', bundle_offers.view, name="view_bundle_offer"),
    url(r'^bundle_offers/(?P<bundle_offer_id>\d+)/edit/?$', bundle_offers.edit, name="edit_bundle_offer"),
    url(r'^bundle_offers/(?P<bundle_offer_id>\d+)/delete/?$', bundle_offers.delete, name="delete_bundle_offer"),

    # Group offers
    url(r'^group_offers/?$', group_offers.index, name="view_group_offers"),
    url(r'^group_offers/new/?$', group_offers.new, name="new_group_offer"),
    url(r'^group_offers/(?P<group_offer_id>\d+)/?$', group_offers.view, name="view_group_offer"),
    url(r'^group_offers/(?P<group_offer_id>\d+)/edit/?$', group_offers.edit, name="edit_group_offer"),
    url(r'^group_offers/(?P<group_offer_id>\d+)/delete/?$', group_offers.delete, name="delete_group_offer"),
]
