
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, "offers/index.html")