from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Status
from django.utils.translation import gettext_lazy as _


class StatusListView(ListView):
    template_name = "statuses/statuses_list.html"
    model = Status
    context_object_name = "statuses"
