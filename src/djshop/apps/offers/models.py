# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


# A set of products has some discount. This discount can be percentual
class GroupOffer(models.Model):
    DISCOUNT_TYPE = (
        ("percentage", "Percentage"),
        ("absolute", "Absolute")
    )
    name = models.CharField(max_length=128, verbose_name=u"Name of the offer")

    description = models.TextField(verbose_name=u"Description of the offer", default="", blank=True)

    discount_amount = models.DecimalField(verbose_name=u"Discount amount", decimal_places=2, max_digits=10)

    discount_type = models.CharField(verbose_name=u"Discount type (percent or absolute)",
                                     max_length=32, choices=DISCOUNT_TYPE)

    product_categories = models.ManyToManyField("store.ProductCategory", verbose_name=u"ProductCategory",
                                                help_text="Product categories that are contained in this offer", blank=True)

    products = models.ManyToManyField("store.Product",
                                      verbose_name=u"Products", help_text="Products that are contained in this offer",
                                      blank=True)

    creator = models.ForeignKey(User, verbose_name=u"Creator", related_name="created_group_offers")

    # Informs if this group offer is applicable for a shopping cart (a list of selected products)
    def is_applicable(self, selected_products):
        # Ids of the products that must be bought together to enjoy the offer
        group_offer_product_ids = {product.id: True for product in self.products.all()}

        # Ids of the product categories that must be bought together to enjoy the offer
        group_offer_product_category_ids = {product_category.id: True for product_category in self.product_categories.all()}

        # For each one of the products in the shopping cart, we are going to check
        # If it is one of the products that enable this offer and,
        # If it belongs to a product category that enable this offer
        for selected_product in selected_products:
            # If the product is needed to activate this offer, erase it from the needed product list
            if selected_product.id in group_offer_product_ids:
                del group_offer_product_ids[selected_product.id]
            else:
                selected_product_categories = selected_product.categories
                # If this product belongs to one category that is needed to activate this offer,
                # erase that given category from the needed product category list
                for selected_product_category in selected_product_categories:
                    if selected_product_category.id in group_offer_product_category_ids:
                        del group_offer_product_category_ids[selected_product_category.id]
                        break

        # This group offer is applicable if there are no needed products to
        group_offer_applicable = len(group_offer_product_ids.keys()) == 0 and\
                                 len(group_offer_product_category_ids.keys()) == 0
        return group_offer_applicable

    # Return the new price of the shopping cart that enjoys this discount
    def get_discounted_price(self, original_price):
        if self.discount_type == "absolute":
            return float(original_price) - float(self.discount_amount)
        if self.discount_type == "percentage":
            return float(original_price) - float(original_price) * float(self.discount_amount) / 100.0
        raise ValueError("Discount type is not legal")


# A bundle is an packaged offer when buying a certain amount of products gives you some free products.
# For example,
class BundleOffer(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Name of the offer")

    description = models.TextField(verbose_name=u"Description of the offer", default="", blank=True)

    product = models.ForeignKey("store.Product", verbose_name=u"Paid product", related_name="product")

    bundle_product_units = models.PositiveIntegerField(verbose_name=u"Number of units in the bundle", default=3)
    paid_product_units = models.PositiveIntegerField(verbose_name=u"Number of units the customer must pay", default=2)

    creator = models.ForeignKey(User, verbose_name=u"Creator", related_name="created_bundle_offers")

    # Check if the selected product has a discount (3x2, 4x3, etc.)
    def can_apply_discount(self, selected_product):
        if selected_product.product.price_type != "price_per_unit":
            return False
        if selected_product.product.id != self.product.id:
            return False
        if int(selected_product.amount) < int(self.bundle_product_units):
            return False
        return True

    # Get the discounted price for a product
    # None implies it has no discount
    def get_discounted_price(self, selected_product):
        if not self.can_apply_discount(selected_product):
            return None

        # Check if the product is at least a bundle
        if int(selected_product.amount) < self.bundle_product_units:
            return None

        num_of_bundles = int(selected_product.amount) / self.bundle_product_units
        remaining_products = int(selected_product.amount) % self.bundle_product_units

        price_of_bundles = selected_product.product.get_price(num_of_bundles*self.paid_product_units)
        price_of_remaining_products = selected_product.product.get_price(remaining_products)

        return price_of_bundles + price_of_remaining_products
