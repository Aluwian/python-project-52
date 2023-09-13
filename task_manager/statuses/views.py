from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.list import ListView

from .form import CreateStatusForm
from .models import Status
from django.utils.translation import gettext_lazy as _

from ..my_mixins import CustomLoginRequiresMixin


class StatusListView(CustomLoginRequiresMixin, ListView):
    template_name = "statuses/statuses_list.html"
    model = Status
    context_object_name = "statuses"

    def get_queryset(self):
        return Status.objects.order_by("pk")


class CreateStatusView(
    CustomLoginRequiresMixin, SuccessMessageMixin, CreateView
):
    model = Status
    form_class = CreateStatusForm
    template_name = "layout/form.html"
    success_message = _("Status successfully created")
    success_url = reverse_lazy("StatusesList")
    extra_context = {"title": _("Create status"), "button_text": _("Create")}


class UpdateStatusView(
    CustomLoginRequiresMixin, SuccessMessageMixin, UpdateView
):
    model = Status
    form_class = CreateStatusForm
    template_name = "layout/form.html"
    success_message = _("Status successfully updated")
    success_url = reverse_lazy("StatusesList")
    extra_context = {"title": _("Update status"), "button_text": _("Update")}


class DeleteStatusView(
    CustomLoginRequiresMixin, SuccessMessageMixin, DeleteView
):
    model = Status
    template_name = "statuses/delete.html"
    success_message = _("Status delete successfully")
    success_url = reverse_lazy("StatusesList")
    extra_context = {"title": _("Delete status"), "button_text": _("Delete")}
