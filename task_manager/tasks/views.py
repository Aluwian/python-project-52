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
    context_object_name = "tasks"
    extra_context = {
        "button_text": _("Show"),
    }

    def get_queryset(self):
        return Task.objects.order_by("pk")


class TaskView(CustomLoginRequiresMixin, DetailView):
    template_name = "tasks/task_view.html"
    model = Task
    context_object_name = "task"


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


class UpdateTaskView(
    CustomLoginRequiresMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = Task
    form_class = CreateTaskForm
    template_name = "layout/form.html"
    success_message = _("Task successfully updated")
    success_url = reverse_lazy("TasksList")
    extra_context = {"title": _("Update task"), "button_text": _("Update")}


class DeleteTaskView(
    CustomLoginRequiresMixin,
    AuthorPermissionMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Task
    template_name = "tasks/delete.html"
    success_message = _("User deleted successfully")
    success_url = reverse_lazy("TasksList")
    permission_message = _("A task can only be deleted by its author")
    permission_url = reverse_lazy("TasksList")
    extra_context = {"title": _("Delete task"), "button_text": _("Delete")}
