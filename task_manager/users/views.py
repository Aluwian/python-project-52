from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import User
from .form import CreateUserForm


class UsersListView(ListView):
    template_name = "users/users_list.html"
    model = User
    context_object_name = "users"

    def get_queryset(self):
        return User.objects.order_by("pk")


class CreateUserView(SuccessMessageMixin, CreateView):
    form_class = CreateUserForm
    template_name = "users/form.html"
    success_message = "User successfully registered"
    success_url = reverse_lazy("Home")
    extra_context = {"title": "Registration", "button_text": "Registration"}
