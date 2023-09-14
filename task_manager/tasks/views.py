from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.list import ListView
from django.utils.translation import gettext_lazy as _
from .form import CreateTaskForm
from .models import Task
from ..my_mixins import CustomLoginRequiresMixin

class TasksListView(CustomLoginRequiresMixin, ListView):
    