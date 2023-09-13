from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Status


class CreateStatusForm(forms.ModelForm):
    name = forms.CharField(max_length=75, required=True, label=_("Name"))

    class Meta:
        model = Status
        fields = ("name",)
