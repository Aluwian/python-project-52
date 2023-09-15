from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    # UpdateView,
    # DeleteView,
)
from django.views.generic.list import ListView
from django.utils.translation import gettext_lazy as _
from .form import CreateTaskForm
from .models import Task
from ..my_mixins import CustomLoginRequiresMixin


class TasksListView(CustomLoginRequiresMixin, ListView):
    template_name = "tasks/tasks_list.html"
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.order_by("pk")


class CreateTaskView(CustomLoginRequiresMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = "layout/form.html"
    success_message = _("Task successfully created")
    success_url = reverse_lazy("TasksList")
    extra_context = {"title": _("Create task"), "button_text": _("Create")}

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
