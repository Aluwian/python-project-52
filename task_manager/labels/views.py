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
from django.contrib.messages.views import SuccessMessageMixin


class LabelListView(CustomLoginRequiresMixin, ListView):
    template_name = "labels/label_list.html"
    model = Label
    context_object_name = "labels"

    def get_queryset(self):
        return Label.objects.order_by("pk")


class CreateLabelView(
    CustomLoginRequiresMixin, SuccessMessageMixin, CreateView
):
    model = Label
    form_class = CreateLabelForm
    template_name = "layout/form.html"
    success_message = _("Label successfully created")
    success_url = reverse_lazy("LabelsList")
    extra_context = {"title": _("Create label"), "button_text": _("Create")}


class UpdateLabelView(
    CustomLoginRequiresMixin, SuccessMessageMixin, UpdateView
):
    model = Label
    form_class = CreateLabelForm
    template_name = "layout/form.html"
    success_message = _("Label successfully updated")
    success_url = reverse_lazy("LabelsList")
    extra_context = {"title": _("Update label"), "button_text": _("Update")}


class DeleteLabelView(
    CustomLoginRequiresMixin,
    ProtectedDeleteMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Label
    template_name = "labels/delete.html"
    success_message = _("Label deleted successfully")
    success_url = reverse_lazy("LabelsList")
    error_message = _("Cannot delete label because it is in use")
    error_url = reverse_lazy("LabelsList")
    extra_context = {"title": _("Delete label"), "button_text": _("Delete")}
