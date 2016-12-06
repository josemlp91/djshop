# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from decimal import Decimal
from django.contrib.auth.models import User
from django.db import models


# Each product belongs to a category
class ProductCategory(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Name of the product category")
    description = models.TextField(verbose_name=u"Description of the product category", default="", blank=True)

    def __unicode__(self):
        return self.name


# Each one of the products of the shop
class Product(models.Model):
    PRICE_TYPE_CHOICES = (
        ("price_per_serving", "Price per weight"),
        ("price_per_unit", "Price per portion"),
    )

    creator = models.ForeignKey(User, verbose_name=u"Creator", related_name="created_products")

    name = models.CharField(max_length=128, verbose_name=u"Name of the product")

    description = models.TextField(verbose_name=u"Description of the product", default="", blank=True)

    main_image = models.ImageField(verbose_name=u"Main image of the product", default=None, null=True, blank=True)

    price = models.DecimalField(verbose_name=u"Price of this product",
                                help_text="Default price of this product", decimal_places=2, max_digits=10)

    price_type = models.CharField(choices=PRICE_TYPE_CHOICES, max_length=32, default="price_per_weight")

    serving_size = models.ForeignKey("store.ServingSize", blank=True, default=None, null=True)

    max_serving_size = models.PositiveIntegerField("Maximum serving size", default=None, null=True, blank=True)

    min_serving_size = models.PositiveIntegerField("Minimum serving size", default=None, null=True, blank=True)

    is_public = models.BooleanField(verbose_name=u"Is this product visible in the virtual shop?")

    categories = models.ManyToManyField("store.ProductCategory",
                                        verbose_name=u"Product categories", related_name="products")

    def __unicode__(self):
        return self.name

    # Get the price given an specific amount of product (units or grams)
    def get_price(self, amount):
        if self.price_type == "price_per_unit":
            return self.price * Decimal(amount)

        if self.price_type == "price_per_serving":
            serving_weight = self.serving_size.weight
            return (self.price / serving_weight) * Decimal(amount)


# The weighted products have a price according to the amount of product that is served
class ServingSize(models.Model):
    weight = models.PositiveIntegerField(
        verbose_name=u"Weight amount for this price per weight in grams",
        default="100", help_text=u"Weight amount for this price per weight in grams. By default it is 100 g."
    )

    def __unicode__(self):
        return "{0} g".format(self.weight)


