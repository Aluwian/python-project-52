from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .models import User
from .form import CreateUserForm


class UsersListView(ListView):
    template_name = "users/users_list.html"
    model = User
    context_object_name = "users"


class CreateUserView(CreateView):
    form_class = CreateUserForm
    template_name = "users/create.html"
