from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.list import ListView

from .form import CreateLabelForm
from .models import Label
from django.utils.translation import gettext_lazy as _

from ..my_mixins import CustomLoginRequiresMixin, ProtectedDeleteMixin


class LabelListView(CustomLoginRequiresMixin, ListView):
    template_name = "labels/label_list.html"
    model = Label
    context_object_name = "labels"

    def get_queryset(self):
        return Label.objects.order_by("pk")
