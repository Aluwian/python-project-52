from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Label


class CreateLabelForm(forms.ModelForm):
    name = forms.CharField(max_length=75, required=True, label=_("Name"))

    class Meta:
        model = Label
        fields = ("name",)
