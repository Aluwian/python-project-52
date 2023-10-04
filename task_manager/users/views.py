from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.my_mixins import (
    CustomLoginRequiresMixin,
    CustomPermissionRequiredMixin,
    ProtectedDeleteMixin,
)
from .models import User
from .form import CreateUserForm, UpdateUserForm
from django.utils.translation import gettext_lazy as _


class UsersListView(ListView):
    template_name = "users/users_list.html"
    model = User
    context_object_name = "users"


class CreateUserView(SuccessMessageMixin, CreateView):
    model = User
    form_class = CreateUserForm
    template_name = "users/create.html"
    success_message = _("User successfully registered")
    success_url = reverse_lazy("login")


class UpdateUserView(
    CustomLoginRequiresMixin,
    CustomPermissionRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
):
    model = User
    form_class = UpdateUserForm
    template_name = "users/update.html"
    success_url = reverse_lazy("users")
    success_message = _("User updated successfully")
    permission_message = _("You do not have rights to change another user.")
    permission_url = "users"


class DeleteUserView(
    CustomLoginRequiresMixin,
    CustomPermissionRequiredMixin,
    ProtectedDeleteMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = User
    template_name = "users/delete.html"

    success_message = _("User deleted successfully")
    success_url = reverse_lazy("users")

    permission_message = _("You do not have rights to delete another user.")
    permission_url = reverse_lazy("users")

    error_message = _("Cannot delete user because it is in use")
    error_url = reverse_lazy("users")

    extra_context = {"title": _("Delete user"), "button_text": _("Yes, delete")}
