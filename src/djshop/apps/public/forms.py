# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError


# Login form
class LoginForm(forms.Form):
    username = forms.CharField(label=u"Username")
    password = forms.CharField(label=u"Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        user = authenticate(username=cleaned_data.get("username"), password=cleaned_data.get("password"))

        if not user or not user.is_active:
            raise ValidationError(u"Your authentication data is invalid. Please check your username and password")

        cleaned_data["user"] = user
        return cleaned_data


class ShoppingCartCheckoutForm(forms.Form):
    first_name = forms.CharField(label=u"First name")
    last_name = forms.CharField(label=u"Last name")
    telephone_number = forms.CharField(label=u"Telephone number")
    email = forms.EmailField(label=u"Email")
