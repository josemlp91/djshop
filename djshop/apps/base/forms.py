

from django import forms


class DeleteForm(forms.Form):
    confirmed = forms.BooleanField(label=u"Confirm you want to delete this object")

