from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.list import ListView
from django.utils.translation import gettext_lazy as _
from django_filters.views import FilterView

from .form import CreateTaskForm
from .models import Task
from ..my_mixins import (
    CustomLoginRequiresMixin,
    AuthorPermissionMixin,
)
from .filter import FilterTasks


class TasksListView(CustomLoginRequiresMixin, FilterView, ListView):
    template_name = "tasks/tasks_list.html"
    model = Task
    filterset_class = FilterTasks
    ordering = "pk"
    extra_context = {
        "button_text": _("Show"),
    }


class TaskView(CustomLoginRequiresMixin, DetailView):
    template_name = "tasks/task_view.html"
    model = Task
    context_object_name = "task"


class CreateTaskView(CustomLoginRequiresMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = "tasks/create.html"
    success_message = _("Task successfully created")
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTaskView(
    CustomLoginRequiresMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Task
    form_class = CreateTaskForm
    template_name = "tasks/update.html"
    success_message = _("Task successfully updated")
    success_url = reverse_lazy("tasks")


class DeleteTaskView(
    CustomLoginRequiresMixin,
    AuthorPermissionMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Task
    template_name = "tasks/delete.html"
    success_message = _("Task deleted successfully")
    success_url = reverse_lazy("tasks")
    permission_message = _("A task can only be deleted by its author")
    permission_url = reverse_lazy("tasks")
