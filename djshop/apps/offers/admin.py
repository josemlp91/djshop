from django.contrib import admin

from .models import GroupOffer
from .models import BundleOffer

admin.site.register(GroupOffer)
admin.site.register(BundleOffer)