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

from ..my_mixins import CustomLoginRequiresMixin, ProtectedDeleteMixin


class StatusListView(CustomLoginRequiresMixin, ListView):
    template_name = "statuses/statuses_list.html"
    model = Status
    context_object_name = "statuses"


class CreateStatusView(
    CustomLoginRequiresMixin, SuccessMessageMixin, CreateView
):
    model = Status
    form_class = CreateStatusForm
    template_name = "statuses/create.html"
    success_message = _("Status successfully created")
    success_url = reverse_lazy("statuses")


class UpdateStatusView(
    CustomLoginRequiresMixin, SuccessMessageMixin, UpdateView
):
    model = Status
    form_class = CreateStatusForm
    template_name = "statuses/update.html"
    success_message = _("Status successfully updated")
    success_url = reverse_lazy("statuses")


class DeleteStatusView(
    CustomLoginRequiresMixin,
    SuccessMessageMixin,
    ProtectedDeleteMixin,
    DeleteView,
):
    model = Status
    template_name = "statuses/delete.html"

    success_message = _("Status delete successfully")
    success_url = reverse_lazy("statuses")

    error_message = _("Cannot delete status because it is in use")
    error_url = reverse_lazy("statuses")
