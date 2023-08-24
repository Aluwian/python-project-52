from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, DeletionMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.helpers import (
    CustomLoginRequiresMixin,
    CustomPermissionRequiredMixin,
)
from .models import User
from .form import CreateUserForm
from django.utils.translation import gettext_lazy as _


class UsersListView(ListView):
    template_name = "users/users_list.html"
    model = User
    context_object_name = "users"

    def get_queryset(self):
        return User.objects.order_by("pk")


class CreateUserView(SuccessMessageMixin, CreateView):
    form_class = CreateUserForm
    template_name = "layout/form.html"
    success_message = _("User successfully registered")
    success_url = reverse_lazy("Login")
    extra_context = {"title": _("Registration"), "button_text": _("Registrate")}


class UpdateUserView(
    CustomLoginRequiresMixin,
    CustomPermissionRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = User
    form_class = CreateUserForm
    template_name = "layout/form.html"
    success_url = reverse_lazy("UsersList")
    success_message = _("User updated successfully")
    extra_context = {"title": _("User change"), "button_text": _("Update")}


class DeleteUserView(
    CustomLoginRequiresMixin,
    CustomPermissionRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = User
    template_name = "users/delete.html"
    success_message = _("User updated successfully")
    success_url = reverse_lazy("UsersList")
    extra_context = {"title": _("Delete user"), "button_text": _("Delete")}
