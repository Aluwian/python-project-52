from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    # UpdateView,
    # DeleteView,
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


class CreateStatusView(
    CustomLoginRequiresMixin, SuccessMessageMixin, CreateView
):
    model = Status
    form_class = CreateStatusForm
    template_name = "layout/form.html"
    success_message = _("Status successfully created")
    success_url = reverse_lazy("StatusesList")
    extra_context = {"title": _("Create status"), "button_text": _("Create")}
